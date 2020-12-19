from rest_framework import serializers

from jobs.models import JobOffer
class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)


class CountrySerializer(serializers.Serializer):
    code = serializers.CharField(max_length=3)
    name = serializers.CharField(max_length=255)

class JobOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        fields = '__all__'
