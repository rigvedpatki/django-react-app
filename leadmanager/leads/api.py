"""
  Api
"""
from rest_framework import viewsets, permissions
from leads.models import Lead
from leads.serializers import LeadSerializer


class LeadViewSet(viewsets.ModelViewSet):
    """
      Leads ViewSet class
    """
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer
