from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


@python_2_unicode_compatible
class Question(models.Model):
    question_txt = models.CharField(max_length=200)
    put_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_txt

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.put_date >= timezone.now() - datetime.timedelta(days=1)


@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text