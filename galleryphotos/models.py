from django.db import models
from cloudinary.models import CloudinaryField



# Create your models here.
class Image(models.Model):
    # image = models.ImageField(upload_to = 'images/', default = 'images')
    image_url = CloudinaryField('image', blank=True)
    title = models.CharField(max_length=100)
    category = models.ForeignKey('Category',default='', on_delete = models.CASCADE)
    imageDescription = models.CharField(max_length=450)
    image_location = models.ForeignKey('Location',default='', on_delete = models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''
        class method to display images by date posted
        '''
        ordering = ['date_uploaded']

    
    def __str__(self):
        return self.title


    # def upload_image(self,image=None,title=None, category=None, image_location=None, imageDescription=None, date_uploaded=None):
    #     self.image = image if image else self.image
    #     self.title = title if title else self.Title
    #     self.category = category if category else self.category
    #     self.image_location = image_location if image_location else self.image_location
    #     self.imageDescription = imageDescription if imageDescription else self.imageDescription
    #     self.date_uploaded = date_uploaded if date_uploaded else self.date_uploaded 

    @classmethod
    def images(cls):
        images=cls.objects.all()
        return images

    @classmethod
    def search_by_location(cls, value):
        '''
        Method to filter images by location
        '''
        result = cls.objects.filter(image_location__name__icontains=value)
        return result 


    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_category(cls, search_term):
        '''
        Method to filter images by category
        '''
        result = cls.objects.filter(category__category__icontains=search_term)
        return result 


    


class Location(models.Model):
    name = models.CharField(max_length=200, null=True)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(name=value)


class Category(models.Model):
    category = models.CharField(max_length =30)

    @classmethod
    def get_all_categories(cls):
        '''
        Method to get all categories
        '''
        categories = cls.objects.all()
        return categories

    def save_category(self):
        '''
        Method to save category
        '''
        self.save()

    @classmethod
    def delete_category(cls,category):
        cls.objects.filter(category=category).delete()

    
    def __str__(self):
        return self.category





    