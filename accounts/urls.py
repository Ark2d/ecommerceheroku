from django.conf.urls import url
from . import views

urlpatterns = [
    # ---------------------------------------------- Base Routes -------------------------------------------------------
    url(r'^$', views.index, name='index'),
    url(r'^regostro/$', views.register, name='register'),
    url(r'^alterar-dados/$', views.update_user, name='update_user'),
    url(r'^alterar-senha/$', views.update_password, name='update_password'),
]