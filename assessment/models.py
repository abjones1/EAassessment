from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    organization = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.username}"


class Recipient(models.Model):
    email = models.EmailField(max_length=200)
    pin = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.email}"


class Response(models.Model):
    recipient = models.ForeignKey(Recipient, on_delete=models.PROTECT, related_name="recipient")
    data = models.JSONField(blank=True, null=True)
    received_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.recipient}-response"


class Question(models.Model):
    text = models.CharField(max_length=200)
    topic = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.topic}-{self.text[0:20]}..."


class Assessment(models.Model):
    requestor = models.ForeignKey(User, blank=True, on_delete=models.PROTECT, related_name="requestor")
    questions = models.ManyToManyField(Question, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    sent_time = models.DateTimeField(blank=True, null=True)
    recipients = models.ManyToManyField(Recipient, blank=True, related_name="recipients")
    responses = models.ManyToManyField(Response, blank=True)

    def __str__(self):
        return f"{self.requestor}-{self.created_time}"



