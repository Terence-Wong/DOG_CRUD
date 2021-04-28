from django.urls import path
from .api_views import DogListCreate, DogRetrieveUpdateDestroy

urlpatterns = [
    path('', DogListCreate.as_view()),
    path('<int:id>', DogRetrieveUpdateDestroy.as_view()),
]
