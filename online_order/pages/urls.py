from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.NewsPageView ,name='news'),
    path('category/<slug:category_slug>',views.home, name='products_by_category'),
]