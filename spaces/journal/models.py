from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Journal(models.Model):
	journal_title = models.CharField(max_length=50)
	journal_entry = models.TextField()
	written_by = models.ForeignKey(User, on_delete=models.CASCADE, default="")
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return reverse('journal:journal_detail', kwargs={'pk': self.pk})

	def __str__(self):
		return self.journal_title

class Dgroup(models.Model):
	dgroup_name = models.CharField(max_length=50)
	members = models.ManyToManyField(User, blank=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.dgroup_name