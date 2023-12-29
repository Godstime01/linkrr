from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserModel(AbstractUser):
    profile_image = models.ImageField(
        upload_to='profile_image', default='default.png', null=True, blank=True)
    fullname = models.CharField(max_length=299)
    description = models.CharField(max_length=100, blank=True, null=True)


class Links(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    # user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
