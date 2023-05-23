from django.db import models


# Create your models here.

# 用户模型
class User(models.Model):
    username = models.CharField(max_length=50)
    passwd = models.CharField(max_length=20)
    introduction = models.CharField(max_length=200, default='')

    def toDict(self):
        return {
            'id': self.id,
            'username': self.username,
            'passwd': self.passwd,
            'introduction': self.introduction,
        }

    class Meta:
        db_table = 'user'


# 文件模型
class File(models.Model):
    author_id = models.IntegerField(default=0)
    file_name = models.CharField(max_length=50)
    file_type = models.CharField(max_length=10, default='')
    file_status = models.IntegerField(default=1)
    file_lenth = models.IntegerField(default=0)
    file_path = models.CharField(max_length=100, default='')

    def toDict(self):
        return {
            'file_id': self.id,
            'file_name': self.file_name,
            'file_type': self.file_type,
            'file_lenth': self.file_lenth
        }

    class Meta:
        db_table = 'file'
