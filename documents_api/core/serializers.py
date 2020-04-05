from rest_framework import serializers
from .models import Metadata , Document


class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = ['name','string']


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['name','file']