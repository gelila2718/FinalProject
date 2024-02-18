from django.urls import path
from . import views

# from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.AboutPageView, name="about"),
    path("store/", views.StorePageView, name="store"),
]
