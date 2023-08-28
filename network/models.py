from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    following = models.ManyToManyField(
        'User', blank=True, related_name="followingUser")


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    date = models.DateTimeField()
    likedBy = models.ManyToManyField(User, blank=True, related_name="likedBy")

    def __str__(self):
        return f"{self.id} : {self.user} posts -> {self.content} on {self.date}"



    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.username,
            "content": self.content,
            "date": self.date.strftime("%b %-d, %-I:%M %p")
        }
