
from django.core.validators import MinValueValidator
from uuid import uuid4
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Institute(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    name = models.CharField(blank=False, null=True,
                            editable=True, max_length=255)
    mail = models.EmailField(max_length=255)
    logo = models.URLField(
        default='https://firebasestorage.googleapis.com/v0/b/stately-pulsar-343510.appspot.com/o/static%2Fdeflogo.png?alt=media&token=d99783e2-c80c-4e4f-9300-f85f6aacac50')
    signature = models.URLField(
        default='https://firebasestorage.googleapis.com/v0/b/stately-pulsar-343510.appspot.com/o/static%2Fdefsignature.png?alt=media&token=a53e5c47-51e3-46cd-b415-4ca6e053e969')
    contact = PhoneNumberField()

    def __str__(self):
        return self.name


class Student(models.Model):

    degree_choices = {
        'BE': 'Bachelors in Engineering',
        'B.Tech': 'Bachelors of Technology',
        'BSc': 'Bachelors of Science'
    }

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    roll = models.IntegerField()
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    mobile = PhoneNumberField()
    dob = models.DateField()
    graduating_year = models.IntegerField(max_length=4)
    degree = models.CharField(choices=degree_choices,
                              max_length=255, default='BE')
    address = models.CharField(max_length=255)
    wallet = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.institute.name} {self.roll}'


class Academic_Records(models.Model):
    id = models.UUIDField(primarykey=True, default=uuid4,
                          editable=False, primary_key=True)
    semester = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(
        blank=False, null=False, editable=True, max_length=255)
    grade = models.CharField(blank=False, null=False,
                             editable=True, max_length=2)
    marks = models.IntegerField(null=True, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.id