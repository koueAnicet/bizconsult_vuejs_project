"""bizconsult URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include,re_path
#----
from django.conf import settings
from django.conf.urls.static import static
#----
from rest_framework import routers
from webApp.urls_api import router as webApp_router
#--
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

#----
from graphene_django.views import GraphQLView

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
#ajouter router
router = routers.DefaultRouter()
#creation locale
#route api webapp
router.registry.extend(webApp_router.registry)



urlpatterns = [
    path ( 'jet/' ,  include ( 'jet.urls' ,  'jet' )),   # Django JET URLs
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('', include("webApp.urls")),
    path('api/',include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #------
    path("graphql", GraphQLView.as_view(graphiql=False)),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# permet d'afficher les images
