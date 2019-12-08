from django.contrib import admin

from src.apps.panel.models import ClaimTempModel


@admin.register(ClaimTempModel)
class ClaimTempModelAdmin(admin.ModelAdmin):

    fields = ('__all__',)

