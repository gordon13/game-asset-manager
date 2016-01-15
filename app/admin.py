from django.contrib import admin

from app.models import Asset

class AssetAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)


admin.site.register(Asset, AssetAdmin)
