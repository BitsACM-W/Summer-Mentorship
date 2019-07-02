from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
	author = models.CharField(max_length=200)
	email = models.URLField(default='')
	contact = models.IntegerField(default=0)
	noofblogs = models.IntegerField(default=0)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()