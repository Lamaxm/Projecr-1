from django.db import models
from user_app.models import User

class comment(models.Model):
    """model for comments"""
    name=models.CharField(max_length=50, verbose_name="الاسم")
    body=models.TextField(verbose_name="التعليق")
    comment_date=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=False)
    profile=models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self) -> str:
        return 'علق {} على {} {}'.format(self.name, self.profile,self.id)

class courses(models.Model):
    """model for courses"""
    name = models.CharField(max_length=50)
    description = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class available_time(models.Model):
    """model for courses"""
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)