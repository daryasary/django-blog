from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=30)
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s , %s"%(self.name, self.slug)

class Tag(models.Model):
	name = models.CharField(max_length=30)
	slug = models.SlugField(blank=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super(Tag, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s , %s"%(self.name, self.slug)


class Post(models.Model):
	title = models.CharField(max_length=30)
	body = models.TextField()
	cat = models.ManyToManyField(Category)
	tag = models.ManyToManyField(Tag)
	publish = models.BooleanField()
	slug = models.SlugField(blank=True)

	# default datetime.now should set, next ;)
	# would be hidden field.
	date = models.DateField(default=datetime.now()) 
	author = models.ManyToManyField(User)
	
	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		self.date = datetime.now()
		super(Post, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s, %s" %(self.title , self.body)

class Comment(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField()
	date = models.DateField()
	website = models.URLField(blank=True)
	post = models.ManyToManyField(Post)
	body = models.TextField()

	def __unicode__(self):
		return "%s, %s" %(self.name, self.body)
