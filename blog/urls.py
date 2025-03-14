from django.urls import path
from blog.views import blog_single,blog_view

app_name = 'blog'

urlpatterns = [
    path('',blog_view,name='index'),
    path('single',blog_single,name='single'),

]
