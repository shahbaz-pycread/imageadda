from django.db import models


class Image(models.Model):
    picture = models.ImageField()
    place = models.CharField(max_length=200)

    def __str__(self):
        return "pic clicked at the " + self.place

# Contact Model


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=120)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "You've received the message from " + self.name
