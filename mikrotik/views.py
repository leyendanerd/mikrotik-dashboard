from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from .models import MikrotikDevice


class DeviceListView(ListView):
    model = MikrotikDevice
    template_name = "device_list.html"
    context_object_name = "devices"


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "user_list.html"
    context_object_name = "users"
