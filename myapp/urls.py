from django.urls import path
from django.urls.conf import include
from . import views

app_name='myapp'

urlpatterns = [
    path('',views.home,name='home'),


]