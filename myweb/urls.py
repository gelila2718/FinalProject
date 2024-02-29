from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.AboutPageView, name="about"),
    path("contact/", views.ContactPageView, name="contact"),
    path("store/", views.StorePageView, name="store"),
    path('view_item/<int:product_id>/', views.view_item, name='view_item'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
