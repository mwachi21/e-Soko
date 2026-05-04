from django.db import models
from django.contrib.auth.models import User
import django.db.models.signals

# Create your models here.
# Profile pictures
class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   image = models.ImageField(default='default.jpg', upload_to='profile_pics')
   follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)

   def __str__(self):
      return f'{self.user.username} Profile'
   
# Create or update user profile when user is created or updated
def create_profile(sender, instance, created, **kwargs):
   if created:
      user_profile = Profile(user=instance)
      user_profile.save()
      # User to follow themselves by default after account creation
      user_profile.follows.set([instance.profile.id])
      user_profile.save()

django.db.models.signals.post_save.connect(create_profile, sender=User)