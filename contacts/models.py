from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
from django.db import models
class Contact(models.Model):
    Name = models.CharField(max_length=100, unique=True)  # Ensure name is unique
    Email = models.EmailField(unique=True)  # Ensure email is unique
    Notes = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('contact_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.Name  # Changed from self.name to self.Name
