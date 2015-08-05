from django.contrib import admin

import models

# Define ModelAdmin calsses here:
class TagAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']

class PostAdmin(admin.ModelAdmin):
	# tag = TagAdmin()
	list_display = ['title', 'get_cat', 'publish', 'date', 'get_tags']

class CommentAdmin(admin.ModelAdmin):
	list_display = ['name', 'body', 'email']

# Register your models here.
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, CommentAdmin)