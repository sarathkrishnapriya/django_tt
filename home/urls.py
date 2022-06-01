from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('about',views.about),
    path('booking',views.booking),
    path('contact',views.contact),
]