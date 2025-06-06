from django.shortcuts import render, redirect
from main.models import Articles, Answers
from django.views.generic.detail import DetailView
from .forms import AnswersForm
from datetime import datetime
from django.shortcuts import get_object_or_404


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/otvet_vopros.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем форму в контекст
        context['form'] = AnswersForm()
        # Добавляем список ответов
        context['answers'] = self.object.answers.all()
        return context

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Articles, pk=1)
        comments = Answers.objects.filter(question=post)
        # Получаем текущий объект (вопрос)
        self.object = self.get_object()
        form = AnswersForm(request.POST)
        if form.is_valid():
            # Создаём новый ответ
            answer = form.save(commit=False)
            answer.question = self.object
            answer.date = datetime.now()
            answer.user_id = request.user.id  # Предполагается, что пользователь авторизован
            answer.save()
            return redirect(self.request.path)  # Перенаправляем на ту же страницу

        # Если форма невалидна, возвращаем страницу с ошибками
        context = self.get_context_data()
        context['form'] = form
        context['answers'] = comments
        print(context['answers'])
        return self.render_to_response(context)


def questions(request):
    questions = Articles.objects.all()
    return render(request, 'news/questions.html', {'questions': questions})

