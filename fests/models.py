from django.db import models

class User(models.Model):
	Name = models.CharField(max_length=50)
	Email = models.EmailField()
	def __str__(self):
		return self.Name
