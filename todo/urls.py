from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', TodoList.as_view(), name='list'),
    re_path(r'^(?P<pk>\d)$', IndivTodo.as_view(), name='indiv'),
    path('create/', MakeNotify.as_view(), name='create')
]