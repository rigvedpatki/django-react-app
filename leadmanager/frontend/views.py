"""
  Inserting React application
"""
from django.shortcuts import render


def index(request):
    """
      Inserting the index.html file here
    """
    return render(request, 'frontend/index.html')
