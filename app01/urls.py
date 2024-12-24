"""
URL configuration for app01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_book/',views.add_book),
    path('add_book2/',views.add_book2),
    path('add_book_f/',views.add_book_find),
    path('', views.index),

    path('terminal/', views.getterminal),
    path('test/',views.test),
    path('api/', include('upload.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 配置文件访问
