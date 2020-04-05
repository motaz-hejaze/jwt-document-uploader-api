from . import views
from django.urls import path

urlpatterns = [
    path('metadata' , views.MetaDataListCreate.as_view() , name="metadata_list_create"),
    path('metadata/<name>' , views.MetaDataRetrieve.as_view() , name="metadata_retrieve"),
    path('document' , views.DocumentListCreate.as_view() , name="metadata_list_create"),
    path('document/<name>' , views.DocumentRetrieve.as_view() , name="metadata_retrieve"),
]