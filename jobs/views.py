from django.db.models import Q
from jobs.serializers import CategorySerializer, CountrySerializer, JobOfferSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from jobs.models import Category, Country, JobOffer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticated]


class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    # permission_classes = [IsAuthenticated]


class JobOfferList(generics.ListAPIView):
    serializer_class = JobOfferSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = JobOffer.objects.all()
        q = self.request.query_params.get('q', None)
        if q is not None:
            query = Q(position__icontains=q)
            query.add(Q(description__icontains=q), Q.OR)
            query.add(Q(company__name__icontains=q), Q.OR)
            queryset = queryset.filter(query)
        return queryset


class JobOfferDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializer
    # permission_classes = [IsAuthenticated]
