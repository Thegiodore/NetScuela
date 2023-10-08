from django.urls import path
from .views import *

urlpatterns = [
    path('signup', SignUpCreateView.as_view(), name='signup'),
    path('login', LoginCreateView.as_view(), name='login'),
]