from django.urls import path

from jobs.views import CategoryList, CountryList, JobOfferList, JobOfferDetail

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='categories'),
    path('countries/', CountryList.as_view(), name='countries'),
    path('jobs/', JobOfferList.as_view(), name='jobs'),
    path('jobs/', JobOfferList.as_view(), name='jobs'),
    path('jobs/<uuid:pk>/', JobOfferDetail.as_view()),
]
