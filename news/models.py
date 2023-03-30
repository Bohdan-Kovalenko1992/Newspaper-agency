from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Newspaper(models.Model):
    title = models.CharField(max_length=63)
    content = models.TextField()
    published_date = models.DateField()
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="topic",
    )
    publishers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="newspapers")

    def __str__(self):
        return f"{self.title}"
