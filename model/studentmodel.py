from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    def __init__(self,name,age,phonenumber):
        self.name=name
        self.age=age
        self.phonenumber=phonenumber



       

