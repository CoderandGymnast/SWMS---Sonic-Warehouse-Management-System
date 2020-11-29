import datetime
import random

from django.db import models
from django.utils import timezone

class Product(models.Model):

	name = models.CharField(max_length=255)
	price = models.IntegerField()
	code = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class List(models.Model):

	name = models.CharField(max_length=255)
	notes = models.CharField(blank=True, max_length=255)
	completed = models.BooleanField(default=False, editable=False)
	published_date = models.DateTimeField(default=timezone.now(), verbose_name="Published Date")

	def __str__(self):
		return self.name

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.published_date <= now

	was_published_recently.admin_order_field = "published_date"
	was_published_recently.boolean = True
	was_published_recently.short_description = "Publishded recently?"

class Item(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	list = models.ForeignKey(List, on_delete=models.CASCADE)
	quantity = models.IntegerField()

class Section(models.Model):

	list = models.OneToOneField(List, on_delete=models.CASCADE)
	published_date = models.DateTimeField(default=timezone.now(), verbose_name="Published Date")

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.published_date <= now

	was_published_recently.admin_order_field = "published_date"
	was_published_recently.boolean = True
	was_published_recently.short_description = "Publishded recently?"

class Video(models.Model):
	section = models.ForeignKey(Section, on_delete=models.CASCADE)

