from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "price", ]
    ordering = ["title", "author", "price", ]
    search_fields = ["author", "title", ]
    sortable_by = ["price", "author", "title", ]


admin.site.register(Book, BookAdmin)