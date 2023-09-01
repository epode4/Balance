from django.db import models
from django.conf import settings

# Create your models here.

class Question(models.Model):
    question_a = models.CharField(max_length=100)
    question_b = models.CharField(max_length=100)

    # click_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='click_questions')

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    click = models.CharField(max_length=100)