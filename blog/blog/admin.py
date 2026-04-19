from django.contrib import admin
from .models import Post, Category, Tag, Comment

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(Comment)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name", )
    prepopulated_fields = {"slug": ("name",)}



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category")
    autocomplete_fields = ("tags", )
    prepopulated_fields = {"slug": ("title",)}