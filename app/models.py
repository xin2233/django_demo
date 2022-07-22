from django.db import models

# Create your models here.
# 用户信息


class User(models.Model):
    # 用户表

    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'

import uuid
import datetime
from django.db import models

def image_upload_to(instance, filename):#文件的时间戳
    # print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    id = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace('-','').replace(' ','').replace(':','')
    filename = filename.replace('.csv','_')+id+'.csv'
    # print(filename)
    return 'file/+{filename}'.format(uuid=uuid.uuid4().hex, filename=filename)

class Processlog(models.Model):
    '''日志单模型类'''
    file_name = models.FileField(upload_to=image_upload_to,null=False,blank=False)
    upload_time = models.DateTimeField(auto_now_add=True)
    download_time = models.DateTimeField(null=True,blank=True)
    # username = models.ForeignKey(User, on_delete=models.CASCADE, to_field='name')

