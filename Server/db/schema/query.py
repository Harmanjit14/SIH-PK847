from .types import *
import graphene
import os
from db.utils import *
from db.models import *
from graphql import GraphQLError
from server.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
from db.utils import UploadCSVUtil, get_semester_certifcate_context, get_other_certifcates_context, render_to_pdf


class Query(graphene.ObjectType):

    all_institutes = graphene.List(InstituteType)

    # NLP Engine Quries
    semester_certificate = graphene.String(sem=graphene.Int(required=True))
    migration_certificate = graphene.String()
    character_certificate = graphene.String()

    # Institute Portal Queries
    get_all_students = graphene.List(StudentType, degree=graphene.String(
        required=True), graduating_year=graphene.Int(required=True))
    get_all_sem_subjects = graphene.List(SubjectType, sem=graphene.Int(
        required=True), degree=graphene.String(required=True), graduating_year=graphene.Int(required=True))
    get_all_student_participated = graphene.List(
        ParticipantsType, id=graphene.String(required=True))
    get_all_institute_events = graphene.List(EventType)
    get_all_sem_subjects = graphene.List(SubjectType, sem=graphene.Int(
        required=True), degree=graphene.String(required=True), graduating_year=graphene.Int(required=True))

    # Get delivery persons info
    get_delivery_persons = graphene.List(DeliveryUtil)

    # Flutter App Queries
    student_login = graphene.Field(StudentType)
    student_marks = graphene.List(AcadamicRecordsType)
    student_requests = graphene.List(CertificateRequestType)
    student_participation = graphene.List(EventParticipant)
    student_prize_participation = graphene.List(ParticipantsType)

    def resolve_student_requests(elf, info):
        usr = info.context.user
        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        student = Student.objects.get(user=usr)

        if student == None:
            raise GraphQLError('Not valid Student')

        records = Certificate_Request.objects.filter(
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

    def resolve_get_all_students(self, info, degree, graduating_year):
        usr = info.context.user

        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        teacher = Teacher.objects.get(user=usr)

        if teacher == None:
            raise GraphQLError('Not a valid teacher')

        records = Student.objects.filter(institute=teacher.institute).filter(graduating_year=graduating_year).filter(degree=degree).order_by(
            '-graduating_year').order_by('degree')

        return records

    def resolve_get_all_sem_subjects(self, info, sem, degree, graduating_year):

        usr = info.context.user

        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        teacher = Teacher.objects.get(user=usr)
        if teacher == None:
            raise GraphQLError('Not a valid teacher')

        subjects = Semester_Subject_Registration.objects.filter(institute=teacher.institute).filter(
            graduating_year=graduating_year).filter(semester=sem).filter(degree=degree)

        return subjects

    def resolve_get_all_student_participated(self, info, id):
        usr = info.context.user

        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        teacher = Teacher.objects.get(user=usr)
        if teacher == None:
            raise GraphQLError('Not a valid teacher')

        student_list = EventParticipant.objects.filter(id=id)

        return student_list

    def resolve_get_all_institute_events(self, info):

        usr = info.context.user

        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        student = Student.objects.get(user=usr).institute
        teacher = Teacher.objects.get(user=usr).institute

        if student == None and teacher == None:
            raise GraphQLError("No Valid Student or Teacher")

        if student != None:
            event_list = InstituteEvent.objects.filter(
                institute=student)
            return event_list

        if teacher != None:
            event_list = InstituteEvent.objects.filter(
                institute=teacher)
            return event_list
        return []

    def resolve_get_delivery_persons(self, info):

        usr = info.context.user

        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        manager = Manager.objects.get(user=usr)

        if manager == None:
            raise GraphQLError('Not a valid person')

        records = Delivery.objects.filter(manager=manager)

        return records

    def resolve_student_participation(self, info):
        usr = info.context.user

        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        student = Student.objects.get(user=usr)
        if student == None:
            raise GraphQLError('Not a valid teacher')

        student_list = EventParticipant.objects.filter(student=student)

        return student_list

    def resolve_student_prize_participation(self, info):
        usr = info.context.user

        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        student = Student.objects.get(user=usr)
        if student == None:
            raise GraphQLError('Not a valid teacher')

        student_list = EventParticipant.objects.filter(
            student=student).filter(winner=True)

        return student_list
