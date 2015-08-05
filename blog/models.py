from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

from django.utils.timezone import now

# Create your models here.
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


class Post(models.Model):
	title = models.CharField(max_length=30)
	body = models.TextField()
	cat = models.ManyToManyField(Category)
	tag = models.ManyToManyField(Tag)
	publish = models.BooleanField()
	slug = models.SlugField(blank=True)

	# default datetime.now should set, next ;)
	# would be hidden field.
	date = models.DateField(default=now()) 
	author = models.ManyToManyField(User)

	class Meta:
		ordering = ['-date']
	
	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		self.date = now()
		super(Post, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s" %(self.title)

	def get_absolute_url(self):
		# return "/blog/post/%s" %self.slug
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
	date = models.DateField(default=now())
	website = models.URLField(blank=True)
	post = models.ManyToManyField(Post)
	body = models.TextField()

	def __unicode__(self):
		return "%s, %s" %(self.name, self.body)
