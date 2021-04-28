from .models import Dog
from .serializers import DogSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class DogListCreate(ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class DogRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

