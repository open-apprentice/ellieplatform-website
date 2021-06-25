from django.contrib import admin
from .models import Post, Category, Profile


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'category', 'published_date', 'status')
    list_filter = ('status', 'created_date', 'published_date', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}  # SEO friendly URLs
    raw_id_fields = ('author',)
    date_hierarchy = 'published_date'
    ordering = ('status', 'published_date')
    save_as = True  # removes Save and Add another button with save as new to create a duplicate
    save_on_top = True  # provides the Save and delete also on top of the admin area.


admin.site.register(Category)
admin.site.register(Profile)
