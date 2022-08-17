from django.contrib.auth.models import User
from graphene_django import DjangoObjectType
from db.utils import *
from db.models import *


class UserType(DjangoObjectType):
    class Meta:
        model = User


class InstituteType(DjangoObjectType):
    class Meta:
        model = Institute


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class SubjectType(DjangoObjectType):
    class Meta:
        model = Semester_Subject_Registration


class AcadamicRecordsType(DjangoObjectType):
    class Meta:
        model = Academic_Record


class ManagerUtil(DjangoObjectType):
    class Meta:
        model = Manager


class DeliveryUtil(DjangoObjectType):
    class Meta:
        model = Delivery


class CertificateRequestType(DjangoObjectType):
    class Meta:
        model = Certificate_Request


class ParticipantsType(DjangoObjectType):
    class Meta:
        model = EventParticipant


class EventType(DjangoObjectType):
    class Meta:
        model = InstituteEvent
