from django.urls import path

from jobs.views import CategoryList, CountryList

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='categories'),
    path('countries/', CountryList.as_view(), name='countries'),
]
