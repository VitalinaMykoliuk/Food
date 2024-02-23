from django.urls import path
from products.views import index, about, news, contact, recipes, services, single


app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('news', news, name='news'),
    path('contact', contact, name='contact'),
    path('recipes', recipes, name='recipes'),
    path('services', services, name='services'),
    path('single', single, name='single'),
]