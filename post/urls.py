from django.urls import path
from django.conf.urls import handler404
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.details, name='details'),
    path('create_post', views.create_post, name='create_post'),
    path('edit_post/<int:pk>', views.edit_post, name='edit_post'),
    path('remove_post/<int:pk>', views.remove_post, name='remove_post'),
    path('notallowed', views.not_allowed, name='not_allowed')
]

handler404 = views.custom_404