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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
