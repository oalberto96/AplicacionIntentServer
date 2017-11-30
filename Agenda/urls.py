from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api$', views.get_user_list, name='contactos')
]
