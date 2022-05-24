from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_header=u"这是你能看的地方吗"
admin.site.site_title = u"个人管理界面-非礼勿视"

admin.site.register(models.User)