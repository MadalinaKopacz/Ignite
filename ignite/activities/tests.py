from django.test import TestCase

from activities.models import Activity

class ActivitiesModelsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Activity.objects.create(name = 'reading a book?', description = 'Choose a book from your library and read it!', location = 'at home', location_type = 'indoor', lon = 0, lat = 0)
        

    def test_name_label(self):
        activity = Activity.objects.get(id =1)
        field_label = activity._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
    
    def test_location_type_default(self):
        activity = Activity.objects.get(id =1)
        value = activity._meta.get_field('location_type').default
        self.assertEqual(value, 'any')

    def test_lon_max_lenght(self):
        activity = Activity.objects.get(id=1)
        max_length = activity._meta.get_field('lon').max_digits
        self.assertEqual(max_length, 10)

