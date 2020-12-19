from django.db import models
from django.utils.text import gettext_lazy as _

from common.models import CommonData, ErrorMessages


class Country(CommonData):
    model_name = 'Country'

    name: str = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, field='name')
    )

    def __str__(self):
        return self.name
