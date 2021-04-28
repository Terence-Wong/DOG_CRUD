from django.db import models
from dog.models import Dog

# Create your models here.
class Toy(models.Model):
    name = models.CharField(max_length = 30)
    weight = models.DecimalField(max_digits = 6, decimal_places = 2)
    fun_rating = models.IntegerField(choices=((i, str(i)) for i in range(1, 6)))
    owner = models.ForeignKey(to=Dog, on_delete=models.CASCADE)


