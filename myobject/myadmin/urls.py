"""myobject URL Configuration

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
# from django.contrib import admin
from django.urls import path

from .views import index, member, user, shop

urlpatterns = [
    # 后台首页
    path('', index.index, name="myadmin_index"),
    # 会员管理路由
    # path('member/<int:pindex>', member.index, name="myadmin_member_index"),  # 浏览会员

    # 员工账号信息管理
    path('user/<int:pindex>', user.index, name="myadmin_user_index"),  # 浏览信息
    path('user/add', user.add, name="myadmin_user_add"),  # 加载添加表单
    path('user/insert', user.insert, name="myadmin_user_insert"),  # 执行信息添加
    path('user/del/<int:uid>', user.delete, name="myadmin_user_del"),  # 删除信息
    path('user/edit/<int:uid>', user.edit, name="myadmin_user_edit"),  # 准备信息编辑
    path('user/update/<int:uid>', user.update, name="myadmin_user_update"),  # 执行信息编辑
    # 重置员工密码
    # path('user/resetpass/<int:uid>', user.resetpass, name="myadmin_user_resetpass"),
    # path('user/doresetpass/<int:uid>', user.doresetpass, name="myadmin_user_doresetpass"),

    # 后台管理员路由
    path('login', index.login, name="myadmin_login"),
    path('dologin', index.dologin, name="myadmin_dologin"),
    path('logout', index.logout, name="myadmin_logout"),
    path('verify', index.verify, name="myadmin_verify"),  # 验证码

    # 店铺路由
    path('shop/<int:pindex>', shop.index, name="myadmin_shop_index"),
    path('shop/add', shop.add, name="myadmin_shop_add"),
    path('shop/insert', shop.insert, name="myadmin_shop_insert"),
    path('shop/del/<int:sid>', shop.delete, name="myadmin_shop_del"),
    path('shop/edit/<int:sid>', shop.edit, name="myadmin_shop_edit"),
    path('shop/update/<int:sid>', shop.update, name="myadmin_shop_update"),
]
