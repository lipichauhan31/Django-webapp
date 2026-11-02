from django.contrib import admin

from .models import User, Customer

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'number')
    
admin.site.register(User,UserAdmin)
admin.site.register(Customer,CustomerAdmin)