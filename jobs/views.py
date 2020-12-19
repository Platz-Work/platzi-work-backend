from jobs.serializers import CategorySerializer, CountrySerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from jobs.models import Category, Country


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]