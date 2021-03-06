from .models import Toy
from .serializers import ToySerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class ToyListCreate(ListCreateAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer

class ToyRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer

