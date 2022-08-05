from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image



# Post will contain the various fields that will be populated by the user when writing
class Post(models.Model): 
    postMedia = models.ImageField(null=True, blank=True, upload_to="pics")
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(
        default=timezone.now
    )  # Uses current time from timezone
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # overriding save method to resize images over 800 px
        img = Image.open(self.postMedia.path)
        if img.height > 800 or img.width > 800:
            output_size = (800, 800)
            img.thumbnail(output_size)
        img.save(self.postMedia.path)
            

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})