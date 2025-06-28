"""
URL configuration for labtech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from rest_framework import routers

from appointments.routers.appointments_routers import router as appointments_router
from services.routers.services_routers import router as services_router
from categories.routers.categories_routers import router as categories_router
from content.routers.content_routers import router as content_router
from content.routers.content_routers import router as content_router
from contact.routers.contact_routers import router as contact_router
from branches.routers.branches_routers import router as branch_router
from social.routers.social_router import router as social_router
from faqs.routers.faqs_routers import router as faqs_router
from dashboard.router.dashboard_routers import router as dashboard_router
from account.router.account_routers import router as account_router


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static







router = routers.DefaultRouter()
router.registry.extend(appointments_router.registry)
router.registry.extend(services_router.registry)
router.registry.extend(categories_router.registry)
router.registry.extend(content_router.registry)
router.registry.extend(contact_router.registry)
router.registry.extend(branch_router.registry)
router.registry.extend(social_router.registry)
router.registry.extend(faqs_router.registry)
router.registry.extend(dashboard_router.registry)
router.registry.extend(account_router.registry)


schema_view = get_schema_view(
   openapi.Info(
      title="LabTech API",
      default_version='v1',
      description="LabTech Backend System",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ameetrajak300000@gmail.com"),
      license=openapi.License(name="No License"),
      **{'x-logo': {'url': 'https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png'}},
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('chaining/', include('smart_selects.urls')),
    path('dashboard/', include('dashboard.urls')),    
    path('account/', include('account.urls')),    
    path('services/', include('services.urls')),
    path('appointments/', include('appointments.urls')),
    path('content/', include('content.urls')),
    path('contact/', include('contact.urls')),
    path('categories/', include('categories.urls')),
    path('branches/', include('branches.urls')),
    path('social/', include('social.urls')),
    path('faqs/', include('faqs.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
