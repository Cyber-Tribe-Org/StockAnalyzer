# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('test-redis/', views.test_redis, name='test_redis'),
]
