from django.urls import path
from .views import *

urlpatterns = [
    path('authentication', SignUpCreateView.as_view(), name='authentication'),
    path('login', LoginCreateView.as_view(), name='login'),
]