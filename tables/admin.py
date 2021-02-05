from django.contrib import admin

from .models import Word, Table

class TableAdmin(admin.ModelAdmin):
    search_fields = ('title', )

admin.site.register(Word)
admin.site.register(Table, TableAdmin)
