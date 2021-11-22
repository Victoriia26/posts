from django.urls import path
from my_post_app.views import (get_post, detail_post,
                               delete_post, create_post,
                               new_create)

urlpatterns = [
    path('', get_post, name='post'),
    path('detail/<int:pk>/', detail_post, name='detail'),
    path('delete/<int:pk>/', delete_post, name='delete'),
    path('create/', create_post, name='create'),
    path('new-create/', new_create, name='new_create'),
]