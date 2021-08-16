from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    FormView,
    ListView,
    TemplateView,
    UpdateView
)
from polls.models import Answer, Poll, Question
from polls.forms import QuestionForm, PollForm, AnswerForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin


class IsStaffMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class IsSuperuserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class PollTemplateView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('polls')
    template_name = "polls.html"
    extra_context = {"polls": Poll.objects.all()}


class QuestionTemplateView(TemplateView):
    template_name = "questions.html"
    extra_context = {"questions": Question.objects.all()}


class AnswerTemplateView(TemplateView):
    template_name = "answers.html"
    extra_context = {"answers": Answer.objects.all()}


class PollListView(IsStaffMixin, ListView):
    template_name = "list.html"
    model = Poll


class QuestionListView(IsSuperuserMixin, ListView):
    template_name = "list.html"
    model = Question


class AnswerListView(ListView):
    template_name = "list.html"
    model = Answer


class QuestionFormView(FormView):
    template_name = "form.html"
    form_class = QuestionForm
    success_url = reverse_lazy('questions')

    def form_valid(self, form):
        my_question_text = form.cleaned_data["question_text"]
        my_pub_date = form.cleaned_data["pub_date"]
        my_poll = form.cleaned_data["poll"]
        Question.objects.create(question_text=my_question_text, pub_date=my_pub_date, poll=my_poll)
        return HttpResponseRedirect(self.get_success_url())


class PollFormView(FormView):
    template_name = "form.html"
    form_class = PollForm
    success_url = reverse_lazy('polls')

    def form_valid(self, form):
        my_name = form.cleaned_data["name"]
        Poll.objects.create(name=my_name)
        return HttpResponseRedirect(self.get_success_url())


class AnswerFormView(FormView):
    template_name = "form.html"
    form_class = AnswerForm
    success_url = reverse_lazy('answers')

    def form_valid(self, form):
        my_answer_text = form.cleaned_data["answer_text"]
        my_question = form.cleaned_data["question"]
        Answer.objects.create(answer_text=my_answer_text, question=my_question)
        return HttpResponseRedirect(self.get_success_url())


# CRUD
class QuestionCreateView(CreateView):
    model = Question
    template_name = 'form.html'
    # fields = "__all__"
    success_url = reverse_lazy('questions')
    form_class = QuestionForm  # musi być klasą dziedziczącą po ModelForm (a my mamy zwykłe Form) - zmienimy to chyba


class PollCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ("polls.add_poll")
    model = Poll
    template_name = 'form.html'
    # fields = "__all__"
    success_url = reverse_lazy('polls')
    form_class = PollForm  # musi być klasą dziedziczącą po ModelForm (a my mamy zwykłe Form) - zmienimy to chyba


class AnswerCreateView(CreateView):
    model = Answer
    template_name = 'form.html'
    # fields = "__all__"
    success_url = reverse_lazy('answers')
    form_class = AnswerForm  # musi być klasą dziedziczącą po ModelForm (a my mamy zwykłe Form) - zmienimy to chyba


class QuestionDetailView(DetailView):
    model = Question
    template_name = "my_questions.html"  # tu mogło być objects.html
    extra_context = {
        "update_url": "question-update-view",
        "delete_url": "question_delete_view"
    }


class AnswerDetailView(DetailView):
    model = Answer
    template_name = "my_answers.html"
    extra_context = {
        "update_url": "answer-update-view",
        "delete_url": "answer_delete_view"
    }


class PollDetailView(DetailView):
    model = Poll
    template_name = "my_polls.html"
    extra_context = {
        "update_url": "poll-update-view",
        "delete_url": "poll_delete_view"
    }


class QuestionUpdateView(UpdateView):
    model = Question
    fields = ("question_text",)
    template_name = "form.html"
    success_url = reverse_lazy("questions")


class AnswerUpdateView(UpdateView):
    model = Answer
    fields = ("answer_text",)
    template_name = "form.html"
    success_url = reverse_lazy("answers")


class PollUpdateView(UpdateView):
    model = Poll
    fields = ("name",)
    template_name = "form.html"
    success_url = reverse_lazy("polls")


class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'delete.html'
    success_url = reverse_lazy("questions")


class AnswerDeleteView(DeleteView):
    model = Answer
    template_name = 'delete.html'
    success_url = reverse_lazy("answers")


class PollDeleteView(DeleteView):
    model = Poll
    template_name = 'delete.html'
    success_url = reverse_lazy("polls")
