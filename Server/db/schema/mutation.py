from atexit import register
from .types import *

import graphene
from django.contrib.auth.models import User
from db.utils import *
from db.models import *
from graphql import GraphQLError
from db.utils import UploadCSVUtil, get_semester_certifcate_context, get_other_certifcates_context, render_to_pdf


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

class RegisterInEvent(graphene.Mutation):
    register_in_event=graphene.Field(ParticipantsType)

    class Arguments:
        id=graphene.String()
    
    def mutate(self, info, id):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")

        student = Student.objects.get(user=user)
        event=InstituteEvent.objects.get(id=id)

        if student == None:
            raise GraphQLError("Not a valid Student!")

        ret=EventParticipant.objects.get_or_create(event=event, student=student)
        

        return RegisterInEvent(register_in_event=ret)



class DeleteParticiaption(graphene.Mutation):
    deleteParticipant=graphene.String()

    class Arguments:
        id=graphene.String()
    
    def mutate(self,info,id):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")

        student = Student.objects.get(user=user)
        participant=EventParticipant.objects.get(id=id)

        if student == None:
            raise GraphQLError("Not a valid Student!")
        
        participant.delete()
        str="Done!"

        return DeleteParticiaption(deleteParticipant=str)


        



class Add_Certificate_Request(graphene.Mutation):
    certificate_Request= graphene.Field(CertificateRequestType)

    class Arguments:
        semester=graphene.Int()
        certificate=graphene.String(required=True)
        
       

    def mutate(self, info, **kwargs):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")

        student = Student.objects.get(user=user)

        if student == None:
            raise GraphQLError("Not a valid Student!")
        
        ret=Certificate_Request(
            certificate_status=kwargs.get('certificate'),
            student=student,
            semester=kwargs.get('semester')


        )
        ret.save()

        

        return Add_Certificate_Request(certificate_Request=ret)


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


class AddEventInformation(graphene.Mutation):

    event = graphene.Field(EventType)

    class Arguments:
        event_name = graphene.String(required=True)
        host_name = graphene.String(required=True)
        host_contact = graphene.String(required=True)
        event_overview = graphene.String()
        event_description = graphene.String()
        start_date = graphene.String(required=True)
        end_date = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")

        teacher = Teacher.objects.get(user=user)

        if teacher == None:
            raise GraphQLError("Not a Teacher!")

        ret = InstituteEvent(
            event_name=kwargs.get('event_name'),
            host_name=kwargs.get('host_name'),
            host_contact=kwargs.get('host_contact'),
            event_overview=kwargs.get('event_overview'),
            event_description=kwargs.get('event_description'),
            start_date=kwargs.get('start_date'),
            end_date=kwargs.get('end_date'),
            institute=teacher.institute,
        )
        ret.save()

        return AddEventInformation(event=ret)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()
    upload_student_marks_csv = UploadStudentMarksCSV.Field()
    upload_student_data_csv = UploadStudentDataCSV.Field()
    add_new_institute_event = AddEventInformation.Field()
    certificate_Request=Add_Certificate_Request.Field()
    register_participant=RegisterInEvent.Field()
    delete_participant=DeleteParticiaption.Field()
