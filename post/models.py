from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    
    def __str__(self):
        return str(self.pk) + ' | ' + self.title
    
    def formated_date(self):
        return self.pub_date.strftime("%d/%m")
    
    def formated_date_to_input(self):
        return self.pub_date.strftime("%Y-%m-%d")
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.pk) + ' | ' + self.content