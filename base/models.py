from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name

# Model for Room
class Room(models.Model):
    host = models.ForeignKey(User, on_delete= models.SET_NULL, null=True )
    topic = models.ForeignKey(Topic, on_delete= models.SET_NULL, null=True )
    name = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    # participants = 
    updated = models.DateTimeField(auto_now = True) # "auto_now" take a snapshot for time when each time it get updated 
    created = models.DateTimeField(auto_now_add = True) # "auto_now_add" take snapshot each time when object get created, It will never changed

    def __str__(self):
        return self.name
    
#Model for message
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) # CASCADE - It delete all the message associated with room, if the room get deleted
    body = models.TextField()
    updated = models.DateTimeField(auto_now = True) 
    created = models.DateTimeField(auto_now_add = True)

    # create string version
    def __str__(self):
        return self.body[0: 50]