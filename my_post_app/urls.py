from django.urls import path
from my_post_app.views import get_post, detail_post

urlpatterns = [
    path('', get_post, name='post'),
    path('detail/<int:pk>/', detail_post, name='detail')
]