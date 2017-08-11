from django.contrib import admin

import models


class AuthorAdmin(admin.ModelAdmin):
	list_display = ['user', 'display_name']


class TagAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']


class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'author', 'get_cat', 'get_tags', 'publish', 'created_at']
	prepopulated_fields = {'slug':("title",)}

	def save_model(self, request, obj, form, change):
		if getattr(obj, 'author', None) is None:
			# TODO: Check if user don't have author instance raise error 
			if getattr(request.user, 'author', None) is None:
				raise 'User is not available'
			print '#####', request.user.author
			obj.author = request.user.author
		obj.save()


class CommentAdmin(admin.ModelAdmin):
	list_display = ['name', 'body', 'email']


# Register your models here.
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, CommentAdmin)