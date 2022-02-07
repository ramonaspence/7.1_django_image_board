from django.urls import path
from django.conf.urls.static import static

from django.conf import settings
from .views import *

urlpatterns = [
    # path('', Gallery.as_view(), name = 'gallery'),
    path('', Gallery_list.as_view(), name = 'gallery_list'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
