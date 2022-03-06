from django.db import models

# Create your models here. -- データベースを操作するときに利用するファイル
class UserModel(models.Model):  #クラス継承
    user_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


