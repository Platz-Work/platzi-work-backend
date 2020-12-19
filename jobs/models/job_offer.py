from django.db import models
from django.utils.text import gettext_lazy as _

from django_enumfield.enum import EnumField

from common.models import CommonData, ErrorMessages
from jobs.enums import EnglishLevel, Seniority
from jobs.models import Category, Company, Country, Currency, Technology


class JobOffer(CommonData):
    model_name = 'JobOffer'

    position: str = models.CharField(
        verbose_name=_('Position'),
        max_length=100,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, field='position')
    )

    description: str = models.TextField(
        verbose_name=_('Description'),
        error_messages=ErrorMessages.get_field(
            model=model_name, field='description')
    )

    company: Company = models.ForeignKey(
        to=Company,
        on_delete=models.PROTECT,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='company_id')
    )

    seniority: Seniority = EnumField(
        verbose_name=_('Seniority'),
        enum=Seniority,
        default=Seniority.NA,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='seniority')
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
        error_messages=ErrorMessages.get_field(
            model=model_name, field='category_id')
    )

    country: Country = models.ForeignKey(
        to=Country,
        on_delete=models.PROTECT,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='country_id')
    )

    cities: str = models.CharField(
        verbose_name=_('cities'),
        max_length=100,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, field='cities')
    )

    technologies = models.ManyToManyField(
        Technology,
        verbose_name=_('Technologies'),
    )

    soft_skills: str = models.TextField(
        verbose_name=_('Description'),
        null=True,
        blank=True,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='description')
    )

    salary_start: int = models.PositiveIntegerField(
        verbose_name=_('Salary from'),
        error_messages=ErrorMessages.get_field(
            model=model_name, field='salary_start')
    )

    salary_end: int = models.PositiveIntegerField(
        verbose_name=_('Salary up'),
        error_messages=ErrorMessages.get_field(
            model=model_name, field='salary_end')
    )

    currency: Currency = models.ForeignKey(
        to=Currency,
        on_delete=models.PROTECT,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='currency_id')
    )

    benefits: str = models.TextField(
        verbose_name=_('Description'),
        null=True,
        blank=True,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='description')
    )

    is_active: bool = models.BooleanField(
        verbose_name=_('Active'),
        error_messages=ErrorMessages.get_field(
            model=model_name, field='is_active')
    )

    def __str__(self):
        name: str = f'{self.position - self.description}'
        return name[:30]
