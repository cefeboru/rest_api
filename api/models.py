from django.db import models

# Create your models here.
class listItem(models.Model):
	title = models.CharField(max_length=100)
	content = models.CharField(max_length=100)
	status = models.BooleanField()