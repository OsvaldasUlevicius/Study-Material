from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# profile model that has a 1-1 relationship
# 1-1 relationship means that 1 user can have 1 profile and 1 profile will be associated with 1 user

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # if we delete the user from the database, we will also delete the profile/ but if we delete the profile we dont delete the user
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') # need to install pillow

    def __str__(self):
        return '{} Profile'.format(self.user.username)

    def save(self): # overriding the default save method
        super().save() # saving the parent class
        
        img = Image.open(self.image.path) # resizing the image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)