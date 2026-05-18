from django.urls import path
from .views import ContactAPIView, ContactListAPIView

urlpatterns = [
    path("", ContactAPIView.as_view(), name="contact"),
    path("messages/", ContactListAPIView.as_view(), name="contact-messages"),
]
