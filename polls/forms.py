from django.core.exceptions import ValidationError
from django import forms
from polls.models import Poll, Question, Answer
from datetime import datetime
import pytz

utc = pytz.UTC


class PastDateField(forms.DateTimeField):

    def validate(self, value):
        super().validate(value)
        if value >= datetime.today().replace(tzinfo=utc):
            raise ValidationError('Only past dates allowed here.')


class LowercaseLetterField(forms.CharField):
    def validate(self, value):
        super().validate(value)
        if value[0].isupper():
            raise ValidationError('Only lower letters allowed')


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized')


def lowercase_validator(value):
    if value.isupper():
        raise ValidationError("Value must be lower case")


class NameForm(forms.Form):
    name = LowercaseLetterField(max_length=128)
    birth_date = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'eg.2006-10-25 14:30:59'}))


class PollForm(forms.ModelForm):
    name = forms.CharField(max_length=128)

    def clean_name(self):
        return self.cleaned_data["name"].upper()

    class Meta:
        model = Poll
        fields = '__all__'


class QuestionForm(forms.ModelForm): #potem dodam ModelForm i naprawię

    question_text = forms.CharField(max_length=128, validators=[capitalized_validator])
    pub_date = PastDateField(widget=forms.TextInput(attrs={'placeholder': 'eg.2006-10-25 14:30:59'}))
    poll = forms.ModelChoiceField(queryset=Poll.objects.all())

    def clean_question_text(self):
        return self.cleaned_data["question_text"].lower()

    def clean(self):
        cleaned_data = super().clean()
        if not self.errors:
            if cleaned_data["question_text"][0] == "a" and cleaned_data["pub_date"].year < 2000:
                self.add_error("question_text", "Can't start with an 'a'")
                self.add_error("pub_date", "Can't be a date before 2000")
                raise ValidationError("Form invalid. Correct errors and submit again")
            # if cleaned_data["question_text"][0] == "w" and cleaned_data["pub_date"] < datetime.datetime.today().replace(tzinfo=utc):
            #   self.add_error("question_text", "Can't start with a 'w'")
            # self.add_error("pub_date", "Can't be a date from past - FUTURE IS COMING")

            # raise ValidationError("Form invalid. Popraw")
        return cleaned_data
    #na razie to wykomentuję - będę patrzeć później
    class Meta:
        model = Question
        fields = "__all__"




class AnswerForm(forms.ModelForm):
    answer_text = forms.CharField(max_length=128, validators=[lowercase_validator])
    question = forms.ModelChoiceField(queryset=Question.objects.all())

    class Meta:
        model = Answer
        fields = '__all__'
