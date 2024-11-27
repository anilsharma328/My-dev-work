from django.contrib import admin
from newapp.models import Registration
# Register your models here.

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name','email_id','phone_number']

admin.site.register(Registration, RegistrationAdmin)
