from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('booking',views.booking,name='booking'),
    path('contact',views.contact,name='contact'),
    path('Dashboard',views.dashboard,name='dashboard'),
    
]