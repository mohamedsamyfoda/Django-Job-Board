from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

TYPE_OF_Degree=(
    ('Student','Student'),
    ('Bachelor','Bachelor'),
    ('Master', 'Master'),
    ('Doctor', 'Doctor'),

)


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey('City', related_name='user_city', on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile/')
    description = models.TextField(max_length=1000)
    experience = models.TextField(max_length=1000)
    Qualifications = models.TextField(max_length=1000)
    Degree = models.CharField( choices = TYPE_OF_Degree, max_length=50)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    google = models.CharField(max_length=100, blank=True, null=True)



    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)

