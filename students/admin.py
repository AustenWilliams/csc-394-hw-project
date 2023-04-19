from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student
from django.contrib import admin
from .models import Student, Course

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)

