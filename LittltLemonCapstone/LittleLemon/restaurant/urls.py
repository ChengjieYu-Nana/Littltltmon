#define URL route for index() view
from django.urls import path
from . import views
# from .views import menuView,bookingView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'booking',views.BookingViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    # path('menu/',menuView.as_view()),
    # path('booking/',bookingView.as_view()),
    path('menu/',views.MenuItemView.as_view()),
    path('menu/<int:pk>',views.SingleMenuItemView.as_view()),
    # path('booking/',views.BookingViewSet.as_view()),
    # path('booking/<int:pk>',views.SingleBookingView.as_view()),
    path('api-token-auth/',obtain_auth_token),
]

# urlpatterns += router.urls