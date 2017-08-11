from django.contrib import admin

import models

# Define ModelAdmin calsses here:
class TagAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']

class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'get_cat', 'get_tags', 'publish', 'created_at']
	prepopulated_fields = {'slug':("title",)}

	def save_model(self, request, obj, form, change):
		if getattr(obj, 'author', None) is None:
			if hasattr(request.user, 'auther', None):
				raise 'User is not available'
			obj.author = request.user
		obj.save()

class CommentAdmin(admin.ModelAdmin):
	list_display = ['name', 'body', 'email']

# Register your models here.
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, CommentAdmin)