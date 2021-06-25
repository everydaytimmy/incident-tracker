from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
# from django.urls.base import reverse

class Incident(models.Model):
  summary = models.CharField(max_length=256)
  reporter = models.ForeignKey(get_user_model(),on_delete=CASCADE)
  detail = models.TextField()

  def __str__(self):
    return self.summary[:50]

  # def get_absolute_url(self):
  #     return reverse("incident_detail", args=[str(self.id)])
  