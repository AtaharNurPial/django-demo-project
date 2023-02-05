from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ChatRoom(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    participants = models.ManyToManyField(User, 
        related_name='participants', blank=True)    # creates a many-to-many relation between entities
    created_at = models.DateTimeField(auto_now_add=True)  # takes time snapshot once during creation
    updated_at = models.DateTimeField(auto_now=True)    # takes time snapshot everytime an instance is called

    class Meta():
        ordering = ['-updated_at','-created_at']

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)  # "ForeignKey" creates relation between tables/models
    room = models.ForeignKey(ChatRoom,on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta():
        ordering = ['-updated_at','-created_at']

    def __str__(self):
        return self.body
