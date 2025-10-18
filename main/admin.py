from django.contrib import admin
from main.models import Toilets, Comments
# Register your models here.
# admin.site.register(Comments)

@admin.register(Toilets)
class ToiletsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',) }


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    prepopulated_fields = {}