from django.urls import path
from .api_views import ToyListCreate, ToyRetrieveUpdateDestroy

urlpatterns = [
    path('', ToyListCreate.as_view()),
    path('<int:id>', ToyRetrieveUpdateDestroy.as_view()),
]
