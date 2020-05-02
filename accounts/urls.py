from django.conf.urls import url
from . import views

urlpatterns = [
    # ---------------------------------------------- Base Routes -------------------------------------------------------
    url(r'^regostro/$', views.register, name='register'),
]