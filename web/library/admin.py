from django.contrib import admin
from .models import Books, Category


@admin.register(Books)
class MemberAdmin(admin.ModelAdmin):
    """Books model admin"""
    list_display = ['title', 'author','published_date', 'active']
    search_fields = ['title', 'author', 'published_date', 'active']
    list_filter = ['title', 'author', 'published_date', 'active']

@admin.register(Category)
class MemberCategory(admin.ModelAdmin):
    """Books model admin"""
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']