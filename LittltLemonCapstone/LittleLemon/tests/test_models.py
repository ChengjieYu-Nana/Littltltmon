from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def instance(self):
        item = Menu.objects.create(
            title="Icecream",
            price="80",
            inventory="100"
        )
        self.assertEqual(item,"Icecream:80")
        