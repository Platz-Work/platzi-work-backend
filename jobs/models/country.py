from django.db import models
from django.utils.text import gettext_lazy as _

from common.models import CommonData, ErrorMessages


class Country(CommonData):
    model_name = 'Country'

    code: str = models.CharField(
        verbose_name=_('Code'),
        max_length=3,
        unique=True,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, field='code')
    )

    name: str = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
        unique=True,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, field='name')
    )

    def __str__(self):
        return self.code

    class Meta(CommonData.Meta):
        verbose_name_plural = _('Countries')
