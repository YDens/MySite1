from django.contrib import admin
from main.models import Toilets
# Register your models here.
#admin.site.register(Toilets)

@admin.register(Toilets)
class ToiletsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',) }