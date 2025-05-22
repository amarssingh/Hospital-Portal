from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_blog, name='create_blog'),
    path('my-posts/', views.doctor_posts, name='doctor_posts'),
    path('all/', views.patient_blog_view, name='patient_blog_view'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
]
