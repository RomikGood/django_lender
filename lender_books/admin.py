from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added', 'date_borrowed')


admin.site.register(Book, BookAdmin)
