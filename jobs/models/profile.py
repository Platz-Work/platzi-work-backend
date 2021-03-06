from django.db import models
from django.conf import settings
from django.utils.text import gettext_lazy as _

from django_enumfield.enum import EnumField

from common.models import CommonData, ErrorMessages
from jobs.enums import EnglishLevel
from jobs.models import Category, Country


class Profile(CommonData):
    model_name = 'Profile'

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    salary_start: int = models.PositiveIntegerField(
        verbose_name=_('Salary from'),
        null=True,
        blank=True,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='salary_start')
    )

    salary_end: int = models.PositiveIntegerField(
        verbose_name=_('Salary up'),
        null=True,
        blank=True,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='salary_end')
    )

    english_level: EnglishLevel = EnumField(
        verbose_name=_('English level'),
        enum=EnglishLevel,
        default=EnglishLevel.NA,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='english_level')
    )

    category: Category = models.ForeignKey(
        to=Category,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='category_id')
    )

    country: Country = models.ForeignKey(
        to=Country,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='country_id')
    )

    def __str__(self):
        return self.user.name
