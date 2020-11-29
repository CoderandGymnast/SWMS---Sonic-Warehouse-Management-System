from django.db import models

class Product(models.Model):

	name = models.CharField(null=True, max_length=255)
	price = models.IntegerField()
	code = models.IntegerField()

	def __str__(self):
		return self.name
