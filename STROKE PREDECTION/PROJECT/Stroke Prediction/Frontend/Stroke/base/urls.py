from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name="home"),
    path('index', views.index, name='index'),
    path('signup/',views.SignupPage,name='signup'),
    path('demo/', views.demo_view, name='demo'),
    # path('portfolio/', views.PortfolioPage, name='portfolio'),
    # path('upload/', views.upload_image, name='upload_image'),
    path('result', views.result, name='result'),
    path('demo/', views.demo_view, name='demo'),
    path('about/', views.about_view, name='about'),
    
]