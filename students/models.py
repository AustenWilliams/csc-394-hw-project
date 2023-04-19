from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, primary_key=False)
    
    def __str__(self) -> str:
    	return self.first_name + " " + self.last_name

class Course(models.Model):
    department = models.CharField(max_length=60)
    number = models.CharField(max_length=3)
    students = models.ManyToManyField(Student)
    
    def __str__(self) -> str:
        return self.department + "-" + self.number