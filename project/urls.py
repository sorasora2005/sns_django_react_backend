"""
URL configuration for project project.

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
from django.urls import path, include
from todo.views import ToDoViewSet
from user_profile.views import ProfileViewSet, user_profile_list

from rest_framework import routers
from django.conf import settings

from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'todo', ToDoViewSet)
router.register(r'user_profile', ProfileViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('user_profile_list/', user_profile_list, name='user_profile_list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)