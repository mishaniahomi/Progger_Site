from django.contrib import admin
from .models import Test, Category


class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'difficulty', 'category')
    list_display_links = ('id', 'title', 'difficulty')
    search_fields = ('title', 'description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )

    
admin.site.register(Test, TestAdmin)
admin.site.register(Category, CategoryAdmin)