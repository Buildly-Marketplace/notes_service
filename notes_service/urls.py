"""notes_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path
from rest_framework import permissions, routers
from notes import views

# openapi implementation
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

swagger_info = openapi.Info(
        title="Notes Service",
        default_version='latest',
        description="Collect and share notes from a single event from multiple third party note service apis",
)

schema_view = get_schema_view(
    swagger_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)              

router = routers.SimpleRouter()

router.register(r'noteprovider', views.NoteProviderViewSet)
router.register(r'notes', views.NoteViewSet)
router.register(r'userregistration', views.UserRegistrationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
        re_path(r'^docs/swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('health_check/', include('health_check.urls')),

]

urlpatterns += staticfiles_urlpatterns()

