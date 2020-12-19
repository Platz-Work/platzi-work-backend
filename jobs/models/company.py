from django.db import models
from django.utils.text import gettext_lazy as _

from common.models import CommonData, ErrorMessages


class Company(CommonData):
    model_name = 'Company'

    name: str = models.CharField(
        verbose_name=_('Name'),
        max_length=255,
        error_messages=ErrorMessages.get_char_field(
            model=model_name, field='name')
    )

    description: str = models.TextField(
        verbose_name=_('Description'),
        error_messages=ErrorMessages.get_field(
            model=model_name, field='description')
    )

    site_url: str = models.URLField(
        verbose_name=_('Site URL'),
        error_messages=ErrorMessages.get_char_field(
            model=model_name, field='site_url', max_length=200)
    )

    def __str__(self):
        return self.name

    class Meta(CommonData.Meta):
        verbose_name_plural = _('Companies')