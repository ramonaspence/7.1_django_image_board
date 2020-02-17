from django.urls import path
from .views import gallery_page_view

urlpatterns = [
    path('', gallery_page_view, name = 'gallery')
]
