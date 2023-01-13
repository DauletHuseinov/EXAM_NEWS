"""exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from account import views as acc_view
from news import views as new_view
from rest_framework.routers import DefaultRouter


acc_router = DefaultRouter()
acc_router.register('register', acc_view.AuthorRegisterAPIView)

new_router = DefaultRouter()
new_router.register('news', new_view.NewsAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),

    path('api/account/', include(acc_router.urls)),
    path('api/', include(new_router.urls)),
    path('api/news/<int:news_id>/comment/<int:comment_id>', new_view.CommentAPIView.as_view())
]
