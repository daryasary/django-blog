from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(User):
	website = models.URLField()
	Image = models.ImageField(blank=True)

	def __unicode__(self):
		return self.username

