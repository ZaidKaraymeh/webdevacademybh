from django.db import models

# Create your models here.


class CourseSignUp(models.Model):
    full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    course = models.CharField(max_length=255)