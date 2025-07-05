from django.db import models


class MikrotikDevice(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(protocol="IPv4")
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name} ({self.ip_address})"

