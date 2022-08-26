from django.core.validators import MinValueValidator
from uuid import uuid4
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from .degree_data import degree_choices
# Create your models here.


class Institute(models.Model):
    institute_choices=(
        ("0","College"),
        ("1","School")
    )
    
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    institute_type = models.CharField(
        choices=institute_choices, default="0", max_length=255, null=False, blank=False)
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


class Manager(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True)
    mobile = PhoneNumberField()
    location = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.location} {self.name}'


class Delivery(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True)
    mobile = PhoneNumberField()
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    state = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class Teacher(models.Model):

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    mobile = PhoneNumberField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.institute.name} {self.name}'


class Student(models.Model):

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    roll = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    mobile = PhoneNumberField()
    dob = models.CharField(max_length=10, blank=True)
    graduating_year = models.IntegerField()
    degree = models.CharField(choices=degree_choices,
                              max_length=255, default='0')
    address = models.CharField(max_length=255, blank=True)
    wallet = models.IntegerField(validators=[MinValueValidator(0)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    batch = models.CharField(blank=True, max_length=255)  # subsections
    father_name = models.CharField(blank=True, max_length=255)
    mother_name = models.CharField(blank=True, max_length=255)
    current_semester = models.IntegerField(default=1, null=True, blank=False)
    passed = models.BooleanField(default=False, null=True)
 

    def __str__(self):
        return f'{self.institute.name} {self.roll}'


class Academic_Record(models.Model):
    id = models.UUIDField(default=uuid4,
                          editable=False, primary_key=True)
    semester = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=255, blank=False, null=False)
    subject = models.CharField(
        blank=False, null=False, editable=True, max_length=255)
    grade = models.CharField(blank=False, null=False,
                             editable=True, max_length=2)
    marks = models.IntegerField(null=True, validators=[MinValueValidator(0)])
    credits = models.FloatField(default=0, null=False, blank=False)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    graduating_year = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f'{self.id} {self.student.institute.name}'


class Academic_Record_File(models.Model):

    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.IntegerField()
    url = models.URLField()

    def __str__(self):
        return self.id


class Semester_Subject_Registration(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    credits = models.FloatField(default=0, null=False, blank=False)
    subject = models.CharField(
        blank=False, null=False, editable=True, max_length=255)
    subject_code = models.CharField(max_length=255, blank=False, null=False)
    semester = models.IntegerField()
    graduating_year = models.IntegerField(blank=False, null=False)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    degree = models.CharField(choices=degree_choices,
                              max_length=255, default='0')

    def __str__(self):
        return f'{self.subject_code} {self.institute.name}'


class Certificate_Request(models.Model):

    delivery_choices = (
        ("0", "Accepted"),
        ("1", "Transit"),
        ("2", "Delivered"),
        ("3", "Failed Attempt"),
        ("4", "Expired"),
        ("5", "Waiting"),
        ("6", "Rejected"),
    )
    certificate_choices = (
        ("0", "Semester Certificate"),
        ("1", "Migration Certificate"),
        ("2", "Domicile Certificate"),
        ("3", "Affadavit"),
        ("4", "Character Certificate"),
        ("5", "Event"),

    )

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    delivery_status = models.CharField(
        choices=delivery_choices, default="5", max_length=255, null=False, blank=False)
    certificate_status = models.CharField(
        choices=certificate_choices, default="1", max_length=255, null=False, blank=False)
    delivery_manager = models.ForeignKey(
        Manager, null=True, blank=True, on_delete=models.SET_NULL)
    delivery_man = models.ForeignKey(
        Delivery, null=True, blank=True, on_delete=models.SET_NULL)
    payment_amount = models.IntegerField(default=0)
    payment_status = models.BooleanField(default=False)
    delivery_done = models.BooleanField(default=False)
    semester = models.IntegerField(blank=True, null=True)
    added = models.DateField(auto_now_add=True, null=True)
    hardcopy_requested = models.BooleanField(default=False, null=True)
    event_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"


class Payment_Receipt(models.Model):

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    payment = models.IntegerField(default=0)
    payment_status = models.BooleanField(default=False)
    paymentid = models.CharField(max_length=255)
    request = models.ForeignKey(Certificate_Request, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"


class InstituteEvent (models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    event_name = models.CharField(
        blank=False, null=False, editable=True, max_length=255)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    host_name = models.CharField(blank=True, max_length=255)
    host_contact = models.CharField(blank=True, max_length=255)
    event_overview = models.CharField(
        max_length=255, default="No Information", null=True)
    event_description = models.TextField(default="No Information", null=True)
    event_ended = models.BooleanField(null=False, default=False)
    start_date = models.CharField(
        blank=False, null=True, editable=True, max_length=255)
    end_date = models.CharField(
        blank=False, null=True, editable=True, max_length=255)

    def __str__(self):
        return f'{self.id} {self.event_name} {self.institute.name}'


class EventParticipant(models.Model):
    prize_choices = (
        ("1", "First"),
        ("2", "Second"),
        ("3", "Third"),
        ("4", "Participant"),
        ("5", "Special Prize")

    )
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    event = models.ForeignKey(InstituteEvent, on_delete=models.CASCADE)
    winner = models.BooleanField(default=False)
    prize = models.CharField(
        choices=prize_choices, default="4", max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.student.roll} {self.event.event_name}'
