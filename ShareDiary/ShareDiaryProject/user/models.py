from django.db import models

# Create your models here. -- データベースを操作するときに利用するファイル

# ユーザーマスタ
class M_USER(models.Model):  #クラス継承
    user_id = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    insert_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now_add=True)

# ユーザーの友達マスタ
class M_USER_FRIENDS(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    frind_user_id = models.CharField(max_length=100, primary_key=True)
    share_start_datetime = models.DateTimeField(auto_now_add=True)
    insert_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now_add=True)

# 日記トラン
class T_DIARY(models.Model):
    diary_id = models.CharField(max_length=100)
    diary_title = models.CharField(max_length=100)
    diary_text = models.CharField(max_length=250)
    post_user_id = models.CharField(max_length=100)
    post_datetime = models.DateTimeField(auto_now_add=True)
    insert_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now_add=True)
    
