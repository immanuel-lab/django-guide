# admin_honeypot/urls.py
from django.urls import path
from admin_honeypot.views import AdminHoneypot

app_name = "admin_honeypot"

urlpatterns = [
    path("", AdminHoneypot.as_view(), name="index"),  # /admin/
    path("<path:url>/", AdminHoneypot.as_view(), name="trap"),  # /admin/anything/
]
