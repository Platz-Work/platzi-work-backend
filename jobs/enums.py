from enum import Enum

from django.utils.text import gettext_lazy as _
from django_enumfield.enum import Enum as DjangoEnum


class EnglishLevel(DjangoEnum):
    NA = 0
    HIGH = 1
    MEDIUM = 2
    LOW = 3

    __labels__ = {
        NA: _('Does not apply'),
        HIGH: _('High'),
        MEDIUM: _('Medium'),
        LOW: _('Low'),
    }


class Seniority(DjangoEnum):
    NA = 0
    SENIOR = 1
    MID_LEVEL = 2
    JUNIOR = 3

    __labels__ = {
        NA: _('Does not apply'),
        SENIOR: _('Senior'),
        MID_LEVEL: _('Mid level'),
        JUNIOR: _('Junior'),
    }
