from django.contrib import admin
from django.contrib.admin import AdminSite
from djangoseo.admin import register_seo_admin, get_inline
from modeltranslation.admin import TranslationAdmin

from blog.seo import BasicMetadata
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

    def get_inline_instances(self, request, obj=None):
        inlines = super(PostAdmin, self).get_inline_instances(request, obj=None)
        if BLOG_SETTINGS['ADD_META']:
            inlines.append(get_inline(BasicMetadata))
        return inlines

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

register_seo_admin(admin.site, BasicMetadata)

# register blog to it's custom admin panel
blog_admin_site = BlogCustomAdmin(name='blog_admin')
blog_admin_site.register(Author, AuthorAdmin)
blog_admin_site.register(Tag, TagAdmin)
blog_admin_site.register(Category, CategoryAdmin)
blog_admin_site.register(Post, PostAdmin)
blog_admin_site.register(Comment, CommentAdmin)

register_seo_admin(blog_admin_site, BasicMetadata)
