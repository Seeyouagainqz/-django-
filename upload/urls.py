from django.urls import path

from .views import ImageUploadView
from . import views
# urlpatterns = [
#     path('upload', views.upload, name='index')
# ]


urlpatterns = [
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
    path('upload_page', views.upload_page, name='index'),
]
