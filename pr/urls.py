"""
URL configuration for pr project.

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
from django.urls import path ,include
from django.conf.urls import url
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('professor/',ProfessorView.as_view(),name='professor' ),
    path('Course/' ,CourseView.as_view(),name='course' ),
    path('Room/',RoomView.as_view(),name='room'),
    path('group/',GroupView.as_view(),name='group'),
    path('calss/',ClassView.as_view(),name='class'),
    path('yearstudent/',Year_studentView.as_view(),name='yearstudent'),
    path('coursinfo/',courseview2.as_view(),name='courseinfo'),
]
