from django.db import models

# Create your models here.

class Article(models.Model):    # 상속
    # id는 자동으로 만들어짐
    title = models.CharField(max_length=10)     # 글자수를 10으로 제한
    content = models.TextField()    # 텍스트로 많은 양의 글을 받을수 있게 함
    created_at = models.DateTimeField(auto_now_add=True)    # 생성시간 자동추가
