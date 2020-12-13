from django.contrib import admin
from .models import Book, Review


class ReviewInline(admin.TabularInline):
    model = Review

class BookAdmin(admin.ModelAdmin):
    inlines = [ReviewInline]
    list_display = ["title", "author", "price", ]
    ordering = ["title", "author", "price", ]
    search_fields = ["author", "title", ]
    sortable_by = ["price", "author", "title", ]


admin.site.register(Book, BookAdmin)