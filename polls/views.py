from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Answer, Poll, Question
from polls.forms import AnswerForm, NameForm, PollForm, QuestionForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test


# Create your views here.

def index(request):
    print(request.user.is_authenticated)
    return render(
        request,
        template_name='index.html'
    )

def homepage(request):
    return render(
        request,
        template_name='homepage.html'
    )

def email_check(user):
    return len(user.email) > 0

def long_check(user):
    return len(user.username) > 5


def hello(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request,
        template_name='hello.html',
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
    )


def hello2(request):
    year = request.GET.get("year", "NO YEAR")
    return HttpResponse(f'Hello, world! {year}')


def animals(request):
    animals = request.GET.get('animals', "NO ANIMAL")
    animals_list = animals.split(",")
    return render(
        request,
        template_name='my_template.html',
        context={'animals': animals_list}
    )


def polls(request):
    return render(
        request,
        template_name='polls.html',
        context={"polls": Poll.objects.all()}
    )


def questions(request):
    return render(
        request,
        template_name='questions.html',
        context={"questions": Question.objects.all()}
    )


def answers(request):
    return render(
        request,
        template_name='answers.html',
        context={"answers": Answer.objects.all()}
    )


@login_required(login_url="accounts/login/")
def get_name(request):
    form = NameForm(request.POST or None)
    if form.is_valid():
        return HttpResponse("IT WORKED!")
    return render(
        request,
        template_name="form.html",
        context={"form": form}
    )


@permission_required('polls.add_poll', raise_exception=True)
def poll_form(request):
    form = PollForm(request.POST or None)
    if form.is_valid():
        my_name=form.cleaned_data["name"]
        Poll.objects.create(name=my_name)
        return HttpResponse("IT WORKED!!! Object created")
    return render(
        request,
        template_name="form.html",
        context={"form": form}
    )

@user_passes_test(email_check)
def question_form(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        my_question_text = form.cleaned_data["question_text"]
        my_pub_date = form.cleaned_data["pub_date"]
        my_poll = form.cleaned_data["poll"]
        Question.objects.create(question_text = my_question_text, pub_date = my_pub_date, poll = my_poll)
        return HttpResponse("IT WORKED!!! Object created")
    return render(
        request,
        template_name="form.html",
        context={"form": form}
    )

@user_passes_test(long_check)
def answer_form(request):
    form = AnswerForm(request.POST or None)
    if form.is_valid():
        my_answer_text = form.cleaned_data["answer_text"]
        my_question = form.cleaned_data["question"]
        Answer.objects.create(answer_text = my_answer_text, question=my_question)
        return HttpResponseRedirect(reverse('answers'))
    return render(
        request,
        template_name="form.html",
        context={"form": form}
    )