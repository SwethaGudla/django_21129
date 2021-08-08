from django.contrib import admin
from .models import MUser
# Register your models here.
@admin.register(MUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['batch', 'name', 'type', 'details', 'Seeds', 'quantity']


