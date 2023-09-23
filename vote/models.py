from django.db import models
# Create your models here.

class Question(models.Model):
    questions_text = models.TextField(max_length=200)
    pub_time = models.DateTimeField('date publish')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField(max_length=200)
    votes = models.IntegerField(default=0)
