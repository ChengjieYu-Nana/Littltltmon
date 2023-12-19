# from django.test import TestCase
# from restaurant.models import Menu
# from restaurant.serializers import menuSerializer
# class MenuViewTest(TestCase):
#     def setup(self):
#         item = Menu.objects.create(
#             title="Icecream",
#             price="80",
#             inventory="100"
#         )
#         self.assertEqual(item,"Icecream:80")
#     def test_getall(self):
#         queryset = Menu.objects.all()
#         serializer = menuSerializer
#         self.assertEqual(queryset,"Icecream:80")