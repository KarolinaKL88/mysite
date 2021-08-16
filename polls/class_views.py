from django.views import View
from django.shortcuts import render, get_object_or_404
from polls.models import Answer, Poll, Question
from django.http import HttpResponse, HttpResponseRedirect

from polls.forms import AnswerForm, NameForm, PollForm, QuestionForm
from django.urls import reverse

class PollView(View):
    def get(self, request):
        return render(
            request,
            template_name="polls.html",
            context={"polls": Poll.objects.all()}
        )

class QuestionView(View):
    def get(self, request):
        return render(
            request,
            template_name="questions.html",
            context={"questions": Question.objects.all()}
        )


class AnswerView(View):
    def get(self, request):
        return render(
            request,
            template_name="answers.html",
            context={"answers": Answer.objects.all()}
        )


class PollFormView(View):
    def get(self, request):
        form = PollForm()
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )

    def post(self, request):
        form = PollForm(request.POST)
        if form.is_valid():
            my_name = form.cleaned_data["name"]
            Poll.objects.create(name=my_name)
            return HttpResponseRedirect(reverse('polls'))
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )


class AnswerFormView(View):
    def get(self, request):
        form = AnswerForm()
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )

    def post(self, request):
        form = AnswerForm(request.POST)
        if form.is_valid():
            my_answer_text = form.cleaned_data["answer_text"]
            my_question = form.cleaned_data["question"]
            Answer.objects.create(answer_text=my_answer_text, question=my_question)
            return HttpResponseRedirect(reverse('answers'))
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )


class QuestionFormView(View):

    def get(self, request):
        form = QuestionForm()
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )

    def post(self, request):
        form = QuestionForm(request.POST)
        if form.is_valid():
            my_question_text = form.cleaned_data["question_text"]
            my_pub_date = form.cleaned_data["pub_date"]
            my_poll = form.cleaned_data["poll"]
            Question.objects.create(question_text=my_question_text, pub_date=my_pub_date, poll=my_poll)
            return HttpResponseRedirect(reverse('questions'))
        return render(
            request,
            template_name="form.html",
            context={"form": form}
        )


class QuestionDetailView(View):
    def get(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        return render(
            request,
            template_name='my_questions.html',
            context = {'question': question}
        )


class AnswerDetailView(View):
    def get(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)
        return render(
            request,
            template_name='my_answers.html',
            context = {'answer': answer}
        )


class PollDetailView(View):
    def get(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        return render(
            request,
            template_name='my_polls.html',
            context = {'poll': poll}
        )


class QuestionUpdateView(View):
    def get(self, request, pk):
        form = QuestionForm()
        get_object_or_404(Question, pk=pk)
        return render(
            request,
            template_name='form.html',
            context={"form": form}
        )

    def post(self, request, pk):
        form = QuestionForm(request.POST)
        if form.is_valid():
            q = Question.objects.get(pk=pk)
            q.question_text = form.cleaned_data["question_text"]
            q.pub_date = form.cleaned_data["pub_date"]
            q.poll = form.cleaned_data["poll"]
            q.save()
            return HttpResponse("IT WORKED")


class AnswerUpdateView(View):
    def get(self, request, pk):
        form = AnswerForm()
        get_object_or_404(Answer, pk=pk)
        return render(
            request,
            template_name='form.html',
            context={"form": form}
        )

    def post(self, request, pk):
        form = AnswerForm(request.POST)
        if form.is_valid():
            a = Answer.objects.get(pk=pk)
            a.answer_text = form.cleaned_data["answer_text"]
            a.question = form.cleaned_data["question"]
            a.save()
            return HttpResponse("IT WORKED")


class PollUpdateView(View):
    def get(self, request, pk):
        form = PollForm()
        get_object_or_404(Poll, pk=pk)
        return render(
            request,
            template_name='form.html',
            context={"form": form}
        )

    def post(self, request, pk):
        form = PollForm(request.POST)
        if form.is_valid():
            p = Poll.objects.get(pk=pk)
            p.name = form.cleaned_data["name"]
            p.save()
            return HttpResponse("IT WORKED")

class QuestionDeleteView(View):
    def get(self, request, pk):
        get_object_or_404(Question, pk=pk)
        return render(
            request,
            template_name='delete.html' # szablon, w którym jest tylko guzik
             #to będzie tylko guzik, nic dalej nie przekazujemy
        )


    def post(self, request, pk):
        q = Question.objects.get(pk=pk)
        q.delete()
        return HttpResponse("UPS, deleted") #można też zrobić redirect


class AnswerDeleteView(View):
    def get(self, request, pk):
        get_object_or_404(Answer, pk=pk)
        return render(
            request,
            template_name='delete.html' # szablon, w którym jest tylko guzik
             #to będzie tylko guzik, nic dalej nie przekazujemy
        )


    def post(self, request, pk):
        a = Answer.objects.get(pk=pk)
        a.delete()
        return HttpResponse("UPS, deleted") #można też zrobić redirect


class PollDeleteView(View):
    def get(self, request, pk):
        get_object_or_404(Poll, pk=pk)
        return render(
            request,
            template_name='delete.html' # szablon, w którym jest tylko guzik
             #to będzie tylko guzik, nic dalej nie przekazujemy
        )


    def post(self, request, pk):
        p = Poll.objects.get(pk=pk)
        p.delete()
        return HttpResponse("UPS, deleted") #można też zrobić redirect