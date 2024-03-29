from django.shortcuts import redirect, render
from . import models
from app.forms import UserForm, RegisterForm
from logger import logger

# Create your views here.


def index(request):
    # logger.error('Something went wrong!') # Log an error message
    logger.info('in index.html')
    return render(request, 'index.html', locals())


def about(request):
    return render(request, 'about.html', locals())


def product(request):
    return render(request, 'product.html', locals())


def gallery(request):
    return render(request, 'gallery.html', locals())


def contact(request):
    return render(request, 'contact.html', locals())


def product(request):
    return render(request, 'product.html', locals())

def test(request):
    return render(request, 'test.html', locals())

def login(request):
    if request.session.get('is_login', None):  # 如果已经登陆了就直接进入index
        return redirect('/index/')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            vc = request.POST['vc']
            if vc.upper() != request.session['verifycode']:
                message = "验证码不正确！"
                return render(request, 'login.html', locals())
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:  # 哈希值和数据库内的值进行比较
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return render(request, 'login.html', locals())
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login.html', locals())

    login_form = UserForm()
    return render(request, 'login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = password1  # 使用加密密码
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")

from django.http import HttpResponse
def verifycodeValid(request):
    vc = request.POST['vc']
    if vc.upper() == request.session['verifycode']:
        return HttpResponse('ok')
    else:
        return HttpResponse('no')

from django.http import HttpResponse,JsonResponse
from app.models import Processlog

def uploadFileSubmit(request):
    # if 'username' in request.COOKIES:
    #     # 获取记住的用户名
    #     username = request.COOKIES['username']
    # else:
    #     username = ''
    # print(username)
    file = request.FILES.get('file_name')
    # try:
    if file:
        Processlog.objects.create(file_name=file)
        message = 'success!'
        return render(request, 'test.html', locals())
        # return render(request,'test.html',{'message': 1})
    else:
        message = 'failed!'
        return render(request, 'test.html', locals())
                #    {'message': 0})
    # except Exception as e:
    #     print(e)
    #     # 2.使用模板
    #     message = 'failed!'
    #     return render(request, 'test.html', locals())
    #     # return render(request, 'test.html',
    #     #               {'message': 0})