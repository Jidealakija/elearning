from django.urls import path
from .views import homepage, about,courses, contact, team, testimonial, error

urlpatterns = [
    path('', homepage, name='index'),
    path('about/', about, name='about'),
    path('courses/', courses, name='courses'),
    path('contact/', contact, name='contact'),
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial'),
    path('404/', error, name='error')
]