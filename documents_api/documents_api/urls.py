from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


description = """
<hr>
<ul>
        <li><h2>No Authorization Required</h2></li>
        <li><p>To signup use link : "auth/users/" </p></li>
        <li><p>To login - create jwt use link : "auth/jwt/create/" </p></li>
        <li><p>Then use Authorize Button to the right and but : [Bearer GeneratedKey] in Bearer text input</p></li>
</ul>

<ul>
        <li><h2>Authorization Required</h2></li>
        <li><p>To List / Create Metadata use link [GET|POST] : "/api/metadata" </p></li>
        <li><p>To Retrieve Metadata use link [GET] : "/api/metadata/<name>" </p></li>
</ul>

<ul>
        <li><h2>Authorization Required</h2></li>
        <li><p>To List / Create Document use link [GET|POST] : "/api/document" </p></li>
        <li><p>To Retrieve Document use link [GET] : "/api/document/<name>" </p></li>
</ul>
<hr>
<h1>Please : If upload using openapi didn't work , please consider using postman</h1>
"""

schema_view = get_schema_view(
   openapi.Info(
      title="Metadata + Document API",
      default_version='v1',
      description=description,
      #license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
