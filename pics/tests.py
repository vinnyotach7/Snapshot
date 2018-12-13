from django.test import TestCase
from .models import Location, Category, Image


# Create your tests here.
class LocationTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.vinny= Location(location = 'London')

    def test_instance(self):
        self.assertTrue(isinstance(self.vinny,Location))

    def test_save_method(self):
        self.vinny.save()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        self.vinny.save()
        self.vinny.delete()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

class CategoryTestClass(TestCase):

    def setUp(self):
        self.category= Category(name = 'Quemn')

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    def test_save_method(self):
        self.category.save()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

class ImageTestClass(TestCase):

    def setUp(self):
        vinny= Location(location = 'London')
        vinny.save()
        self.image= Image(image = 'vinny', image_name = 'image name', description = 'description', location = vinny)
        
        # Creating a new tag and saving it image
        self.new_category = Category(name = 'testing')
        self.new_category.save()

        self.new_image= Image(image = 'Test Image',image_name = 'This is a random test Post', description = 'description',location = vinny)
        self.new_image.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_save_method(self):
            self.image.save()
            images = Image.objects.all()
            self.assertTrue(len(images) > 0)
