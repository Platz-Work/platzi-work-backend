from django.db import models
from django.utils.text import gettext_lazy as _

from common.models import CommonData, ErrorMessages


class Currency(CommonData):
    model_name = 'Currency'

    code: str = models.CharField(
        verbose_name=_('Code'),
        max_length=3,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, field='code')
    )

    name: str = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, field='name')
    )

    to_USD: float = models.FloatField(
        verbose_name=_('To USD'),
        error_messages=ErrorMessages.get_field(
            model=model_name, field='to_USD')
    )

    def __str__(self):
        return self.code
