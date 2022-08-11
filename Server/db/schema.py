
import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType
import os
from db.utils import UploadPDF
from .models import *
from graphql import GraphQLError
from django.db.models import Q
from server.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
from .utils import get_semester_certifcate_context,get_other_certifcates_context, render_to_pdf


class UserType(DjangoObjectType):
    class Meta:
        model = User


class InstituteType(DjangoObjectType):
    class Meta:
        model = Institute


class Query(graphene.ObjectType):

    all_institutes = graphene.List(InstituteType)
    semester_certificate = graphene.String(sem=graphene.Int(required=True))

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


class UploadCSV(graphene.Mutation):

    success = graphene.String()

    class Arguments:
        url = graphene.String(required=True)
        subject = graphene.String(required=True)
        semester = graphene.Int(required=True)
        batch = graphene.Int(required=True)
        institute_id = graphene.String(required=True)

    def mutate(self, info, url, subject, semester, batch, institute_id):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError("Not Logged In!")
        if Academic_Record.objects.filter(semester=semester).filter(
                subject=subject).filter(institute__id=institute_id).filter(batch=batch).exists():
            raise GraphQLError('Data for similar fields already exists')
        ret = UploadPDF(url=url, subject=subject, semester=semester,
                        batch=batch, institute_id=institute_id)
        return UploadCSV(success=ret)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()
    upload_csv = UploadCSV.Field()
