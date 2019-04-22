from django.db import models

# Create your models here.

class Essay(models.Model):
    """
    文章标题
    文章摘要
    文章内容
    文章唯一id
    文章发布日期
    """
    essay_id = models.AutoField(primary_key=True)
    title = models.TextField()
    brief_content = models.TextField()
    content =  models.TextField()
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.title


