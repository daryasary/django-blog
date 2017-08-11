from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

from redactor.fields import RedactorField


class Author(models.Model):
	# Display_name should be available for translation
	display_name = models.CharField(max_length=128)
	avatar = models.ImageField(upload_to='/authors/', null=True)

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
		return "%s , %s"%(self.name, self.slug)

	def get_absolute_url(self):
		from django.core.urlresolvers import reverse
		return reverse ('blog_post_list_cat', args=[str(self.slug)])


class Tag(models.Model):
	name = models.CharField(max_length=30)
	slug = models.SlugField(blank=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super(Tag, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s , %s"%(self.name, self.slug)

	def get_absolute_url(self):
		from django.core.urlresolvers import reverse
		return reverse('blog_post_list_tag', args=[str(self.slug)])


# editor added for body in post, more information
# in : github.com/douglasmiranda/django-wysiwyg-redactor
class Post(models.Model):
	title = models.CharField(max_length=30)
	slug = models.SlugField(blank=True)

	body = RedactorField()
	
	cat = models.ManyToManyField(Category)
	tag = models.ManyToManyField(Tag)

	publish = models.BooleanField(default=True)
	comments_off = models.BooleanField(default=True)

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
		return "%s" %(self.title)

	def get_absolute_url(self):
		from django.core.urlresolvers import reverse
		return reverse('blog_single', args=[str(self.slug)])

	def get_tags(self):
		T = self.tag.all()
		return (', '.join(t.name for t in T))
	get_tags.short_description = 'Tag (s)'

	def get_cat(self):
		C = self.cat.all()
		return (', '.join(c.name for c in C))
	get_cat.short_description = 'Category'


class Comment(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField()
	website = models.URLField(blank=True)
	post = models.ForeignKey(Post, related_name='comments')
	body = models.TextField()

	date = models.DateField(auto_now_add=True)

	def __unicode__(self):
		return "%s, %s" %(self.name, self.body)
