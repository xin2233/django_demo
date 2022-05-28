import imp
from PIL import Image, ImageDraw, ImageFont
# from django.utils.six import BytesIO
from io import StringIO, BytesIO
import random
from django.http import HttpResponse
# /verify_code
def verify_code(request):
    # 引入随机函数模块
   
    # 定义变量，用于画面的背景色、宽、高 RGB
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)

    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    print("rand_str: ",rand_str)

    # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    # font = ImageFont.truetype('FreeMono.ttf', 23)
    # 下面的例子使用MicrosoftSymbol字体，即变量encoding为“symb”，在oxF000和0xF0FF之间绘制一个字符
    # font = ImageFont.truetype('symbol.ttf', 22)
    font = ImageFont.truetype("C:/WINDOWS/Fonts/arial.TTF", 22)
    # font字体的定义要自己去看自己的电脑支持什么（window的字体在    C:\Windows\Fonts 下）ubuntu在/usr/share/fonts，自己去看支持什么就写什么，不要乱写。
    # font = ImageFont.truetype('Arial',22)
    # font = ImageFont.truetype(size= 22)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字

    draw.text((5, 1), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')
