from django.contrib import admin
from .models import Student


# password = admin123
@admin.register(Student)
class StdentAdmin(admin.ModelAdmin):
    list_display =  ["id","name","email"]
# Register your models here.
