from django.contrib import admin
from django.contrib.admin import AdminSite
from modeltranslation.admin import TranslationAdmin

from models import Author, Tag, Category, Post, Comment

from settings import BLOG_SETTINGS


class BlogCustomAdmin(AdminSite):
    site_header = BLOG_SETTINGS['SITE_HEADER']
    site_title = BLOG_SETTINGS['SITE_TITLE']
    index_title = BLOG_SETTINGS['INDEX_TITLE']


class AuthorAdmin(TranslationAdmin):
    # list_display = ['user', 'display_name']
    pass


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'get_cat', 'get_tags',
                    'lang', 'publish', 'created_at']
    prepopulated_fields = {'slug': ("title",)}
    list_filter = ['lang']
    filter_horizontal = ('cat', 'tag')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            if getattr(request.user, 'author', None) is None:
                raise Exception('Author is not available')
            obj.author = request.user.author
        obj.save()


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'body', 'email']


# register blog models to general admin panel
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

# register blog to it's custom admin panel
blog_admin_site = BlogCustomAdmin(name='blog_admin')
blog_admin_site.register(Author, AuthorAdmin)
blog_admin_site.register(Tag, TagAdmin)
blog_admin_site.register(Category, CategoryAdmin)
blog_admin_site.register(Post, PostAdmin)
blog_admin_site.register(Comment, CommentAdmin)
