from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Post

# Creates an instance of of the uploaded image
@receiver(post_save, sender=User)
def create_postMedia(sender, instance, created, **kwargs):
    if created:
        Post.postMedia.create(user=instance) 

# saves instance to users posts.
@receiver(post_save, sender=User)
def save_postMedia(sender, instance, **kwargs):
    instance.Posts.save()
# Not sure if this will work on class based view..
# Safe to delete if not 