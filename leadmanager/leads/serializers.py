"""
  Serializer
"""
# django_rest_framework
from rest_framework import serializers
# leads model
from leads.models import Lead


class LeadSerializer(serializers.ModelSerializer):
    """
      Lead Serializer class
    """
    class Meta:
        model = Lead
        fields = '__all__'
