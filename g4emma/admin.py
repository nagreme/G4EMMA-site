from django.contrib import admin

from .models import Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('filename','upload_date','last_mod_date','document',)
    readonly_fields = ('upload_date','last_mod_date',)

admin.site.register(Document,DocumentAdmin)
