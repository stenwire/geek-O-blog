from django.db import models
from django.contrib.auth.models import User
#from users.utils import image_resize
#from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    '''def save(self, *args, **kwargs):
        image_resize(self.image, 512, 512)
        super().save(*args, **kwargs)'''

    '''def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Profile, self).save()'''

    '''def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)'''
