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
from app import views, viewsUtil, backup
from django.conf import settings
from django.conf.urls.static import static
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
    path('verifycode/', viewsUtil.verifycode), 
    path('verifycode_backup/', backup.verify_code),
    path('verifycodeValid/', views.verifycodeValid), 

    path('uploadFileSubmit/', views.uploadFileSubmit),
]

# 配置用户上传文件url
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #这是关键
