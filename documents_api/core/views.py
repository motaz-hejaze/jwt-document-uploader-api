from django.shortcuts import render
from rest_framework import status , generics
from rest_framework.permissions import IsAuthenticated
from .models import Metadata , Document
from .serializers import MetadataSerializer , DocumentSerializer
from rest_framework.parsers import FileUploadParser
from drf_yasg.utils import swagger_auto_schema
#from drf_yasg import openapi

# Create your views here.

@swagger_auto_schema(tags=["MetaData-List-Create"] ,  request_body=MetadataSerializer , responses={201: 'success', 400: 'errors'})
class MetaDataListCreate(generics.ListCreateAPIView):
    queryset = Metadata.objects.all()
    serializer_class = MetadataSerializer
    permission_classes = [IsAuthenticated]

@swagger_auto_schema(tags=["MetaData-Retrieve"] ,  request_body=MetadataSerializer , responses={201: 'success', 400: 'errors'})
class MetaDataRetrieve(generics.RetrieveAPIView):
    queryset = Metadata.objects.all()
    serializer_class = MetadataSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'name'

@swagger_auto_schema(tags=["Document-List-Create"] ,  request_body=DocumentSerializer , responses={201: 'success', 400: 'errors'})
class DocumentListCreate(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]
    parser_class = (FileUploadParser,)

@swagger_auto_schema(tags=["Document-Retrieve"] ,  request_body=DocumentSerializer , responses={201: 'success', 400: 'errors'})
class DocumentRetrieve(generics.RetrieveAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'name'