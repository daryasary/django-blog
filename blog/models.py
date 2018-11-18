from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from redactor.fields import RedactorField


class Author(models.Model):
    user = models.OneToOneField(User, related_name='author')
    display_name = models.CharField(max_length=128)
    avatar = models.ImageField(upload_to='authors/', blank=True)

    def __unicode__(self, *args, **kwargs):
        return self.display_name


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s , %s" % (self.name, self.slug)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('blog_post_list_cat', args=[str(self.slug)])


class Tag(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s , %s" % (self.name, self.slug)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('blog_post_list_tag', args=[str(self.slug)])


class Post(models.Model):
    header = models.ImageField(upload_to='headers/', blank=True, null=True)
    title = models.CharField(max_length=64)
    slug = models.SlugField(blank=True)

    body = RedactorField()

    cat = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag)

    publish = models.BooleanField(default=True)
    comments_off = models.BooleanField(default=True)

    lang = models.CharField(max_length=8, default=settings.LANGUAGE_CODE,
                            choices=settings.LANGUAGES, verbose_name=_('Language'))

    author = models.ForeignKey(Author, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-modified_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('blog_single', args=[str(self.slug)])

    def get_tags(self):
        return ', '.join(self.tag.values_list('name', flat=True))
    get_tags.short_description = 'Tag (s)'

    def get_cat(self):
        return ', '.join(self.cat.values_list('name', flat=True))
    get_cat.short_description = 'Category'


class Comment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    website = models.URLField(blank=True)
    post = models.ForeignKey(Post, related_name='comments')
    body = models.TextField()

    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s, %s" % (self.name, self.body)
