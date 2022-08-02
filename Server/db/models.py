from uuid import uuid4
from django.db import models

# Create your models here.
class Institute(models.Model):
    id = models.UUIDField(default=uuid4,editable=False,primary_key=True)
    name = models.CharField(blank=False,null=True,editable=True,max_length=255)
    mail = models.EmailField(max_length=255)

    def __str__(self):
        return self.name
    