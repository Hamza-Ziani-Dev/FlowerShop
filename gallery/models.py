from django.db import models


# function upload image
def image_upload(obj,filename):
    imagename, extension = filename.split(".")
    return "gallery/%s/%s.%s"%(obj.id,obj.id,extension)

# Create your models here.
class Flower(models.Model):
    '''
    title
    image
    description
    '''
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=image_upload)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.title