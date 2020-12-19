from django.urls import path

from jobs.views import CategoryList

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='categories')
]