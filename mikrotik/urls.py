from django.urls import path
from .views import DeviceListView, UserListView

urlpatterns = [
    path('', DeviceListView.as_view(), name='device_list'),
    path('users/', UserListView.as_view(), name='user_list'),
]
