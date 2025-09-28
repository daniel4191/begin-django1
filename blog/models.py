from django.db import models

class Post(models.Model):
    title = models.CharField("본문 제목", max_length=100)
    content = models.TextField("본문 내용")
    thumbnail = models.ImageField("썸네일 이미지", upload_to="post", blank = True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField("댓글 내용")
    
    def __str__(self):
        return f"{self.post.title}의 내용 (ID: {self.id})"