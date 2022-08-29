from django.contrib import admin
from .models import InspirationalQuote


class InspirationalQuoteAdmin(admin.ModelAdmin):
    list_display = (
        "custom_name",
        "quote",
    )


admin.site.register(InspirationalQuote, InspirationalQuoteAdmin)
