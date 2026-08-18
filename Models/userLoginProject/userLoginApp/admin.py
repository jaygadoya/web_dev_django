from django.contrib import admin

# Register your models here.
from .models import User
class UserAdmin(admin.ModelAdmin):
    fields = ['user_name','dept']

admin.site.register(User,UserAdmin)