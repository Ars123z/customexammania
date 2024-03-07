# models.py
from django.db import models
from django.contrib.auth import get_user_model

class ChatQuestion(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    question_text = models.TextField()
    answer_text = models.TextField(blank=True, null=True)
    is_answered = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text

