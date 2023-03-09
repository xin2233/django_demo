# myobject/mobile/views/index.py
import datetime

from django.shortcuts import render, redirect, reverse
from myadmin.models import Member


# Create your views here.
def index(request):
    """移动端首页"""
    return render(request, "mobile/index.html")


def register(request):
    """加载注册/登录页面"""
    return render(request, "mobile/register.html")


def doregister(request):
    """执行注册/登录"""
    # 验证短信码
    verifycode = "1234"  # request.session['verifycode']
    code = request.POST['code']
    if verifycode != code:
        context = {'info': '验证码错误！'}
        return render(request, "mobile/register.html", context)

    try:
        # 根据手机号码获取当前会员信息
        member = Member.objects.get(mobile=request.POST['mobile'])
    except Exception as err:
        # print(err)
        # 此处可以执行当前会员注册（添加）
        ob = Member()
        ob.nickname = "顾客"  # 默认会员名称
        ob.avatar = "moren.png"  # 默认头像
        ob.mobile = request.POST['mobile']  # 手机号码
        ob.status = 1
        ob.create_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.update_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ob.save()
        member = ob
    # 检验当前会员状态
    if member.status == 1:
        # 将当前会员信息转成字典格式并存放到session中
        request.session['mobileuser'] = member.toDict()
        # 重定向到登录页
        return redirect(reverse("mobile_index"))
    else:
        context = {"info": '此账户信息禁用！'}
        return render(request, "mobile/register-back.html", context)


def shop(request):
    """ 呈现店铺选择页面 """
    return render(request, "mobile/shop.html")


def selectShop(request):
    """ 执行店铺选择 """
    # 选择好店铺后会跳转到移动端首页
    pass


def addOrders(request):
    """ 加载准备下订单页，由会员确认 """
    return render(request, "mobile/addOrders.html")
