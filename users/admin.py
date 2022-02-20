from django.contrib import admin

from .models import User


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'birth_date', 'address', 'zip_code', 'phone')
    list_display_links = ('id', 'birth_date', 'address', 'zip_code', 'phone')
    search_fields = ('id', 'birth_date', 'address', 'zip_code', 'phone')


admin.site.register(User, AuthorAdmin)
