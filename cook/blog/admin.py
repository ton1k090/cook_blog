from mptt.admin import MPTTModelAdmin

from . import models
from django.contrib import admin


class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'author']
    inlines = [RecipeInline]
    save_as = True
    save_on_top = True


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'website', 'created_at', 'id']


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'prep_time', 'cook_time', 'post']


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)

