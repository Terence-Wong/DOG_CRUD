from django.db import models

# Create your models here.
class Dog(models.Model):

    SEX_CHOICES = [
        # yes or no 
        ('B', 'BOY'),
        ('G', 'GIRL'),
    ]

    name = models.CharField(max_length = 30, default='good boy')
    weight = models.DecimalField(max_digits = 6, decimal_places = 2)
    good_status = models.BooleanField(default=True)
    date_of_birth = models.DateTimeField(auto_now_add=True)
    sex = models.CharField(max_length = 4, choices=SEX_CHOICES)
    fun_rating = models.IntegerField(choices=((i, str(i)) for i in range(1,6)))

