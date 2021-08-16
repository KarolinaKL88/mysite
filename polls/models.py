from django.db import models


# Create your models here.

class Poll(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.id}: {self.name}"


class Question(models.Model):
    question_text = models.CharField(max_length=256)
    pub_date = models.DateTimeField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, null=True, blank=True, related_name='questions')
    def __str__(self):
        return f"{self.id}: {self.question_text}"

class Answer(models.Model):
    answer_text = models.CharField(max_length=128)
    date_added = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    def __str__(self):
        return f"{self.id}: {self.answer_text}"
