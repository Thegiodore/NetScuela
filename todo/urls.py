from django.urls import path

from .views import *

urlpatterns = [
    path('', TodoList.as_view(), name='list'),
    path('1/', IndivTodo.as_view(), name='indiv'),
    path('create/', MakeNotify.as_view(), name='create')
]