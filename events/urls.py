from django.urls import path
from . import views
from django.conf.urls import url
from .views import details

urlpatterns = [
    path('', views.home, name='event-home'),
    path('about/', views.about, name='event-about'),
    url(r'^(?P<id>\d+)/$',details, name = 'details')
]
