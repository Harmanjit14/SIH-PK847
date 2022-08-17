

from importlib.metadata import requires
from typing_extensions import Required



import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType
import os
from db.utils import *
from .models import *
from graphql import GraphQLError
from django.db.models import Q
from server.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
from .utils import UploadCSVUtil, get_semester_certifcate_context, get_other_certifcates_context, render_to_pdf


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
        model = Semester_subject_registration


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
        model = Certificate_Requests

class ParticipantsType(DjangoObjectType):
    class Meta:
        model = Participants


class Query(graphene.ObjectType):

    all_institutes = graphene.List(InstituteType)

    # NLP Engine Quries
    semester_certificate = graphene.String(sem=graphene.Int(required=True))
    migration_certificate = graphene.String()
    character_certificate = graphene.String()

    # Institute Portal Queries
    get_all_students = graphene.List(StudentType)
    get_all_sem_subjects = graphene.List(SubjectType, sem=graphene.Int(required=True), degree=graphene.String(required=True), graduating_year=graphene.Int(required=True))
    get_all_student_participated = graphene.List(ParticipantsType, id=graphene.UUID(required=True))

    # Get delivery persons info
    get_delivery_persons = graphene.List(DeliveryUtil)

    # Flutter App Queries
    student_login = graphene.Field(StudentType)
    student_marks = graphene.List(AcadamicRecordsType)
    student_requests = graphene.List(CertificateRequestType)

    def resolve_student_requests(elf, info):
        usr = info.context.user
        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        student = Student.objects.get(user=usr)

        if student == None:
            raise GraphQLError('Not valid Student')

        records = Certificate_Requests.objects.filter(
            student=student).filter(delivery_done=False)

        return records

    def resolve_student_marks(self, info):
        usr = info.context.user
        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        student = Student.objects.get(user=usr)

        if student == None:
            raise GraphQLError('Not valid Student')

        records = Academic_Record.objects.filter(
            student=student).order_by('-semester')
        return records

    def resolve_student_login(self, info):
        usr = info.context.user
        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        student = Student.objects.get(user=usr)

        if student == None:
            raise GraphQLError('Not valid Student')

        return student

    def resolve_all_institutes(self, info):
        usr = info.context.user
        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        ins = Institute.objects.all()
        return ins

    def resolve_semester_certificate(self, info, sem):

        usr = info.context.user
        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        student = Student.objects.get(user=usr)

        if student == None:
            raise GraphQLError('Not valid Student')

        location = f'static/files/{student.id}sem_{sem}.pdf'
        try:
            context = get_semester_certifcate_context(
                student=student, semester=sem)

            if context['error'] == True:
                raise GraphQLError('Semester data does not exist')

            resp = render_to_pdf('certificate.html', location, context)
            if not resp:
                raise GraphQLError('failed to create certificate')

            mail = EmailMessage(f"Certificate SEM: {sem}",
                                "Here is your ceritificate",
                                EMAIL_HOST_USER,
                                [student.email])
            mail.attach_file(location)
            mail.send()
            os.remove(location)
        except Exception as e:
            # raise GraphQLError(str(e))
            print(e)
            return 'Fail'

        return 'Success'

    def resolve_migration_certificate(self, info):

        usr = info.context.user
        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        student = Student.objects.get(user=usr)

        if student == None:
            raise GraphQLError('Not valid Student')

        location = f'static/files/{student.id}migration.pdf'
        try:
            context = get_other_certifcates_context(student=student)

            if context['error'] == True:
                raise GraphQLError('Semester data does not exist')

            resp = render_to_pdf('migration.html', location, context)
            if not resp:
                raise GraphQLError('failed to create certificate')

            mail = EmailMessage(f"Migration Certificate",
                                "Here is your ceritificate",
                                EMAIL_HOST_USER,
                                [student.email])
            mail.attach_file(location)
            mail.send()
            os.remove(location)
        except Exception as e:
            return str(e)

        return 'Success'

    def resolve_character_certificate(self, info):

        usr = info.context.user
        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        student = Student.objects.get(user=usr)

        if student == None:
            raise GraphQLError('Not valid Student')

        location = f'static/files/{student.id}character.pdf'
        try:
            context = get_other_certifcates_context(student=student)

            if context['error'] == True:
                raise GraphQLError('Semester data does not exist')

            resp = render_to_pdf('character.html', location, context)
            if not resp:
                raise GraphQLError('failed to create certificate')

            mail = EmailMessage(f"Character Certificate",
                                "Here is your ceritificate",
                                EMAIL_HOST_USER,
                                [student.email])
            mail.attach_file(location)
            mail.send()
            os.remove(location)
        except Exception as e:
            # raise GraphQLError(str(e))
            print(e)
            return 'Fail'

        return 'Success'

    def resolve_get_all_students(self, info):
        usr = info.context.user

        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        teacher = Teacher.objects.get(user=usr)

        if teacher == None:
            raise GraphQLError('Not a valid teacher')

        records = Student.objects.filter(institute=teacher.institute).order_by(
            '-graduating_year').order_by('degree')

        return records



    def resolve_get_all_sem_subjects(self, info, sem, degree, graduating_year):

        usr = info.context.user

        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        teacher = Teacher.objects.get(user=usr)
        if teacher == None:
            raise GraphQLError('Not a valid teacher')

        subjects=Semester_subject_registration.objects.filter(institute=teacher.institute).filter(graduating_year=graduating_year).filter(semester=sem).filter(degree=degree)
        
        return subjects

    def resolve_get_all_student_participated(self,info,id):
        usr = info.context.user

        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        teacher = Teacher.objects.get(user=usr)
        if teacher == None:
            raise GraphQLError('Not a valid teacher')
        
        student_list= Participants.objects.filter(id=id)
        return student_list


    def resolve_get_delivery_persons(self, info):
 
        manager = Manager.objects.get(user=usr)

        if manager == None:
            raise GraphQLError('Not a valid person')

        records = Delivery.objects.filter(manager=manager)

        return records



class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email, **kwargs):

        if User.objects.get(username=username):
            raise GraphQLError('User with same username exists')

        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user)


class DeleteUser(graphene.Mutation):
    user = graphene.String()

    def mutate(self, info):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")

        user.delete()
        str = "Done!"

        return DeleteUser(user=str)


class UploadStudentMarksCSV(graphene.Mutation):

    success = graphene.String()

    class Arguments:
        url = graphene.String(required=True)
        subject = graphene.String(required=True)
        subject_code = graphene.String(required=True)
        semester = graphene.Int(required=True)
        graduating_year = graphene.Int(required=True)
        credits = graphene.Int(required=True)

    def mutate(self, info, url, subject, semester, graduating_year, subject_code, credits):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")

        teacher = Teacher.objects.get(user=user)

        if teacher == None:
            raise GraphQLError("Not a Teacher!")

        institute = teacher.institute

        if Academic_Record.objects.filter(semester=semester).filter(
                subject=subject).filter(institute=institute).filter(graduating_year=graduating_year).exists():
            raise GraphQLError('Data for similar fields already exists')

        ret = UploadCSVUtil(url=url, subject=subject, semester=semester,
                            institute=institute, subject_code=subject_code, batch=graduating_year, credits=credits)
        return UploadStudentMarksCSV(success=ret)


class UploadStudentDataCSV(graphene.Mutation):

    success = graphene.String()

    class Arguments:
        url = graphene.String(required=True)
        degree = graphene.String(required=True)
        graduating_year = graphene.Int(required=True)

    def mutate(self, info, url, degree, graduating_year):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")

        teacher = Teacher.objects.get(user=user)

        if teacher == None:
            raise GraphQLError("Not a Teacher!")

        ret = UploadStudentDataUtil(url, teacher, degree, graduating_year)

        return UploadStudentDataCSV(success=ret)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()
    upload_student_marks_csv = UploadStudentMarksCSV.Field()
    upload_student_data_csv = UploadStudentDataCSV.Field()
