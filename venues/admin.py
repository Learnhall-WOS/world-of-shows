from django.contrib import admin

from .models import Venues, GeneralLocation, RequestRent
# Register your models here.


class VenuesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Venues, VenuesAdmin)


admin.site.register([GeneralLocation, RequestRent])