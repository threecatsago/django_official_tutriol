import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    questions_text = models.TextField(max_length=200)
    pub_time = models.DateTimeField('date publish')
    def __str__(self):
        return self.questions_text

    def was_publish_within_one_day(self):
        return timezone.now()-self.pub_time <= datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
