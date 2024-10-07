from django.db import models

# Create your models here.

class Parent(models.Model):
    id = models.AutoField (primary_key= True)


class Child(models.Model):
    field_1 = models.ForeignKey(Parent, related_name = 'children', on_delete = models.CASCADE)
    field_2 = models.CharField(max_length= 50)