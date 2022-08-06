
import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType
from django.core.mail import send_mail
from db.utils import UploadPDF
from .models import *
from graphql import GraphQLError
from django.db.models import Q
from server.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_HOST, EMAIL_BACKEND
from django.core.mail import EmailMessage
from .utils import render_to_pdf


class UserType(DjangoObjectType):
    class Meta:
        model = User


class InstituteType(DjangoObjectType):
    class Meta:
        model = Institute


class Query(graphene.ObjectType):

    all_institutes = graphene.List(InstituteType)
    send_mail = graphene.String()

    def resolve_all_institutes(self, info):
        ins = Institute.objects.all()
        return ins

    def resolve_send_mail(self, info):

        try:
            resp = render_to_pdf('certificate.html', {})
            print(resp)

            mail = EmailMessage("Certificate", "Message goes here", EMAIL_HOST_USER, [
                                'harmanjit140500@gmail.com', 'manroopparmar120@gmail.com'])
            mail.attach_file('certificate.pdf')
            mail.send()
        except Exception as e:
            print(e)
            return str(e)

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
