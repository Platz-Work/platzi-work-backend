from jobs.serializers import CategorySerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from jobs.models import Category


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
