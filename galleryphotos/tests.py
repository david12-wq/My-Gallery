from django.test import TestCase

# Create youfrom django.test import TestCase
from .models import *

# Create your tests here.
class ImageTestClass(TestCase):
    def setup(self):
        self.image_beaches = Image(title='Playa del Amor beach', category='self.image_category', imageDescription = 'Hidden Beach, Playa del Amor, Love Beach - these are all the names of one famous beach in Mexico with the romantic name Love Beach, which is located in a hinged cave.', image_location='self.image_location')

        self.image_location = Location(name='Mexico')
        self.image_loction.save()

        self.image_category = Category(name='Beaches')
        self.image_category.save()

    def test_instance(self):
        self.assertTrue(instance(self.image_beaches, Image))

    def test_save_image(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_image(self):
        self.image.save_image()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue((len(images)==0)) 
        
    def tearDown(self):
        Image.objects.all().delete()
        title.objects.all().delete()
        image_location.objects.all().delete()
        image_category.objects.all().delete()
        imageDescription.objects.all().delete()

    def test_delete_method(self):
        '''
        Method to delete the location
        
        '''
        self.mexico.delete_location('Mexico')
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)

    def tearDown(self):
        '''
        Method that clears the test done on location
        
        '''
        Location.objects.all().delete()



class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(category='Parks to visit')
         self.category.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.Parks to visit, Category))

    def test_save_category(self):
        Category.objects.all().delete()
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        '''
        Method that clears the test done on delete_category
        
        '''
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

    def tearDown(self):
        Category.objects.all().delete()


class LocationTestClass(TestCase):

    #set up method
    def setUp(self):
        '''
        Method to be run in every beginning of the test
        '''
        self.mexico= Location(location='Mexico')

     def test_instance(self):
        self.assertTrue(isinstance(self.mexico, image_location))

    def test_save_method(self):
        '''
        Method to save the location
        
        '''
        self.mexico.save_image_location()
        image_location = image_location.objects.all()
        self.assertTrue(len(image_location)>0)

    def test_delete_method(self):
        '''
        Method to delete the location
        
        '''
        self.mexico.save_image_location('mexico')
        image_location = image_location.objects.all()
        self.assertTrue(len(image_location)==0)

    def tearDown(self):
        image_location.objects.all().delete()r tests here.
