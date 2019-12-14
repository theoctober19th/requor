from django.test import TestCase
from .models import CategoryModel

# Create your tests here.

class CateogoryModelTest(TestCase):
    def setup(self):
        self.django = CategoryModel.objects.create(name='Django', description='Django Unchained')
    
    def test_foobar(self):
        cat = CategoryModel.objects.get(name='Django')
        
        self.assertEqual(cat, 'Django')