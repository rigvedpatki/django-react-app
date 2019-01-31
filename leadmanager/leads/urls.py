"""
  URLs
"""
from rest_framework import routers
from leads.api import LeadViewSet

ROUTER = routers.DefaultRouter()
ROUTER.register('api/leads', LeadViewSet, 'leads')

urlpatterns = ROUTER.urls
