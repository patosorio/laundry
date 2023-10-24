from django.db import models
import uuid

class Invitation(models.Model):
    email = models.EmailField(unique=True)
    sent_on = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)
    token = models.UUIDField(default=uuid.uuid4, unique=True)