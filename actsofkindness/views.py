from .models import AoK
from rest_framework import viewsets, permissions
from .serializers import AoKSerializer

# Create your views here.
class AoKViewSet(viewsets.ModelViewSet):
    # Main Query for Index Route
    queryset = AoK.objects.all()
    
    # Serializer class for serializing output
    serializer_class = AoKSerializer
    
    # STRETCH GOAL: permission class here to set permission level