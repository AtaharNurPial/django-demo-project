from django.db import models

# Create your models here.


class ChatRoom(models.Model):
    # host = 
    # topic = 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    # participants = 
    created_at = models.DateTimeField(auto_now_add=True)  # takes time snapshot once during creation
    updated_at = models.DateTimeField(auto_now=True)    # takes time snapshot everytime an instance is called

    def __str__(self):
        return self.name