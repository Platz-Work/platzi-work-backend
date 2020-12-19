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

        s_start = self.request.query_params.get('salary_start', None)
        if s_start is not None and s_start.isnumeric():
            query = Q(salary_start__gte=int(s_start))
            queryset = queryset.filter(query)

        s_end = self.request.query_params.get('salary_end', None)
        if s_end is not None and s_end.isnumeric():
            query = Q(salary_start__lte=int(s_end))
            queryset = queryset.filter(query)

        category_name = self.request.query_params.get('category', None)
        if category_name is not None :
            query = Q(category__name=category_name)
            queryset = queryset.filter(query)

        english = self.request.query_params.get('english_level', None)
        if english is not None and english.isnumeric():
            query = Q(english_level=int(english))
            queryset = queryset.filter(query)

        country_code = self.request.query_params.get('country', None)
        if country_code is not None :
            query = Q(country__code=country_code)
            queryset = queryset.filter(query)

        return queryset


class JobOfferDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializer
    # permission_classes = [IsAuthenticated]
