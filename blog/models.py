from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


# Defining the model for posts used by db
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # slug = models.SlugField(max_length=255)

    postMedia = models.ImageField(
        default="default.jpg", blank=True, upload_to="post_pics"
    )

    date_posted = models.DateTimeField(
        default=timezone.now
    )  # Uses current time from timezone
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
