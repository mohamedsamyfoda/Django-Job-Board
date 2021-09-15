from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
# Create your models here.

JOB_TYPE =(
    ('FullTime','FullTime'),
    ('PartTime','PartTime')
)


def image_upload(instance , filename):
    imagename , extensin = filename.split(".")
    return "job/%s.%s"%(instance.id , extensin)


class Job(models.Model):
    owner = models.ForeignKey(User, related_name='job_owner',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    des =models.TextField(max_length=100)

    #location
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    description =models.TextField(max_length=1000)
    published_at =models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    modelNum = models.CharField(max_length=100)
    modelTime = models.CharField(max_length=100)

    slug = models.SlugField(blank=True, null=True)


    def save(self, *args,**kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='Apply_job',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter= models.TextField(max_length=500)
    create_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
