from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


# Post will contain the various fields that will be populated by the user when writing
class Post(models.Model):
    postMedia = models.ImageField(default="default.jpg", upload_to="pics" )
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(
        default=timezone.now
    )  # Uses current time from timezone
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # overriding save method to resize images over 300 px
        img = Image.open(self.postMedia.path)
        if img.height > 1024 or img.width > 1024:
            output_size = (1024, 1024)
            img.thumbnail(output_size)
        img.save(self.postMedia.path)