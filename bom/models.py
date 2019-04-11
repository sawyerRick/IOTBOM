from django.db import models


class User(models.Model):
    name = models.CharField(max_length=12, default='None', primary_key=True,verbose_name="用户名")
    password = models.CharField(max_length=100, default='None', verbose_name="密码")
    nick_name = models.CharField(max_length=100, default='None', verbose_name="昵称")
    picture = models.ImageField(upload_to='userimg', default='None', verbose_name="头像")
    email = models.EmailField(default='None', verbose_name="邮箱")
    phone_number = models.CharField(max_length=11, default='None', verbose_name="电话")
    remark = models.CharField(max_length=50, default='None', verbose_name="签名")

    def __str__(self):
        return str(self.name)