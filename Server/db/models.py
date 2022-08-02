from uuid import uuid4
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Institute(models.Model):
    id = models.UUIDField(default=uuid4,editable=False,primary_key=True)
    name = models.CharField(blank=False,null=True,editable=True,max_length=255)
    mail = models.EmailField(max_length=255)

    def __str__(self):
        return self.name
    

class Academic_Records(models.Model):
    id = models.UUIDField(primarykey=True,default=uuid4,editable=False,primary_key=True)
    semester = models.IntegerField()
    student = models.ForeignKey(blank=False,null=False,editable=True,max_length=255)
    subject= models.CharField(blank=False,null=False,editable=True,max_length=255)
    grade= models.CharField(blank=False,null=False,editable=True,max_length=2)
    marks= models.IntegerField(null=True, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.id
    
    