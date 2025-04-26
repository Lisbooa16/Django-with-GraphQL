from django.db import models
from django.utils.translation import gettext_lazy as _

from quiz.choice import ENUM_SCALE, ENUM_TYPE
from quiz.enum import Scale, Type

# Create your models here.
class DataNow(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(DataNow):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Quizzes(DataNow):
    title = models.CharField(max_length=255, default=_(
        "New Quiz"
    ))
    category = models.ForeignKey(
        Category, default=1, on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.title

class Question(DataNow):
    quiz = models.ForeignKey(
        Quizzes, related_name='question', on_delete=models.DO_NOTHING
    )
    technique = models.SmallIntegerField(
        choices=ENUM_TYPE,
        default=Type.MULTIPLE_CHOICE,
        verbose_name="Type of question"
    )
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    difficulty = models.SmallIntegerField(
        choices=ENUM_SCALE,
        default=Scale.FUNDAMENTAL,
        verbose_name="Difficulty"
    )
    is_activate = models.BooleanField(
        default=False, verbose_name=_("Activate Status")
    )

    def __str__(self):
        return self.title

class Answer(DataNow):
    question = models.ForeignKey(
        Question, related_name='answer', on_delete=models.DO_NOTHING
    )
    answer_text = models.CharField(
        max_length=255, verbose_name=_("Answer Text")
    )
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
