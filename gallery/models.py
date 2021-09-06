from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField() 
    category = models.ForeignKey('Category',null=True,on_delete=models.PROTECT)
    location =models.ForeignKey('Location',null=True,on_delete=models.PROTECT)
    image = CloudinaryField('image',default = '')
    # post_date = models.DateTimeField(auto_now_add=True,default=' ')
    
    class Meta:
        # ordering = ['pk']
        verbose_name_plural = 'Images'
    
    def get_image_id(self):
        image_id = self.pk
        return image_id
    
    def save_image(self):
        return Image.objects.save()
    
    def delete_image(self):
        return Image.objects.delete()
    
    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images
    
    @classmethod
    def search_by_title(cls,search_term):
        picha = cls.objects.filter(name__icontains=search_term)
        return picha
    
    def __str__(self):
        return f'{self.name}.{self.description}'
  
class Category(models.Model):
    pic_type = models.CharField(max_length=30)
    
    @classmethod
    def all_categories(cls):
        cat = cls.objects.all()
        return cat
    
    def __str__(self):
        return self.pic_type    

class Location(models.Model):
    location = models.CharField(max_length=30)
    
    @classmethod
    def filter_by_location(cls):
        return cls.objects.filter('location')
    
    def __str__(self):
        return self.location    