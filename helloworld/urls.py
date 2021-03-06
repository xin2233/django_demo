"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app import views 
from captcha.views import captcha_refresh  # 验证码刷新功能，captcha_refresh为captcha.views内置方法，不需要我们单独写

urlpatterns = [

    # 页面响应
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index),
    path('about/', views.about),
    path('product/', views.product),
    path('gallery/', views.gallery),
    path('contact/', views.contact),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('test/', views.test),

    # 动作响应
    path('captcha/', include('captcha.urls')),
    path('refresh/', captcha_refresh),      # 点击可以刷新验证码
]
