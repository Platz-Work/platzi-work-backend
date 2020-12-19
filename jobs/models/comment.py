from django.db import models
from django.utils.text import gettext_lazy as _

from common.models import CommonData, ErrorMessages
from jobs.models import JobOffer, Profile


class Comment(CommonData):
    model_name = 'Comment'

    profile: Profile = models.ForeignKey(
        to=Profile,
        on_delete=models.PROTECT,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='profile_id')
    )

    job_offer: JobOffer = models.ForeignKey(
        to=JobOffer,
        on_delete=models.PROTECT,
        error_messages=ErrorMessages.get_field(
            model=model_name, field='job_offer_id')
    )

    description: str = models.TextField(
        verbose_name=_('Description'),
        error_messages=ErrorMessages.get_field(
            model=model_name, field='description')
    )

    def __str__(self):
        name: str = self.description[:30]
        return f'{self.profile} - {self.job_offer} : {name}'
