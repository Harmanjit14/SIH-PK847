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
    accept_request = graphene.String(id=graphene.String(
        required=True), remarks=graphene.String())
    delete_request = graphene.String(id=graphene.String(
        required=True), remarks=graphene.String())
    get_all_students = graphene.List(StudentType, degree=graphene.String(
        required=True), graduating_year=graphene.Int(required=True))
    get_all_sem_subjects = graphene.List(SubjectType, sem=graphene.Int(
        required=True), degree=graphene.String(required=True), graduating_year=graphene.Int(required=True))
    get_all_student_participated = graphene.List(
        ParticipantsType, id=graphene.String(required=True))
    get_all_institute_events = graphene.List(EventType)
    get_all_sem_subjects = graphene.List(SubjectType, sem=graphene.Int(
        required=True), degree=graphene.String(required=True), graduating_year=graphene.Int(required=True))
    get_all_sem_subjects_for_students = graphene.List(SubjectType, sem=graphene.Int(
        required=True), degree=graphene.String(required=True), graduating_year=graphene.Int(required=True))
    get_all_sem_grades_for_students = graphene.List(
        AcadamicRecordsType, sem=graphene.Int(required=True))
    get_all_request = graphene.List(CertificateRequestType)
    get_all_manager = graphene.List(ManagerUtil)

    # Get delivery persons info
    get_delivery_persons = graphene.List(DeliveryUtil)
    get_manager_request = graphene.List(CertificateRequestType)

    # Flutter App Queries
    student_login = graphene.Field(StudentType)
    student_delete_request = graphene.String(id=graphene.String(
        required=True))
    student_marks = graphene.List(AcadamicRecordsType)
    student_requests = graphene.List(CertificateRequestType)
    student_participation = graphene.List(ParticipantsType)
    student_prize_participation = graphene.List(ParticipantsType)

    def resolve_student_requests(elf, info):
        usr = info.context.user
        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        student = Student.objects.get(user=usr)

        if student == None:
            raise GraphQLError('Not valid Student')

        records = Certificate_Request.objects.filter(
            student=student).filter(verified=False).filter(delivery_done=False)

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
        event = InstituteEvent.objects.get(id=id)
        student_list = EventParticipant.objects.filter(event=event)

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
            raise GraphQLError('Not a valid student')

        student_list = EventParticipant.objects.filter(
            student=student).filter(event__event_ended=False)
        return student_list

    def resolve_student_prize_participation(self, info):
        usr = info.context.user

        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        student = Student.objects.get(user=usr)
        if student == None:
            raise GraphQLError('Not a valid student')

        student_list = EventParticipant.objects.filter(
            student=student).filter(winner=True)

        return student_list

    def resolve_accept_request(self, info, id, remarks=""):
        usr = info.context.user

        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        teacher = Teacher.objects.get(user=usr)
        if teacher == None:
            raise GraphQLError('Not a valid teacher')

        req = Certificate_Request.objects.get(id=id)
        if req == None:
            raise GraphQLError('Not a valid Request')

        cert_index = req.certificate_status
        student = req.student
        if int(cert_index) == 0:
            sem = req.semester
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
                                    f"Here is your ceritificate\n{remarks}",
                                    EMAIL_HOST_USER,
                                    [student.email])
                mail.attach_file(location)
                mail.send()
                os.remove(location)
                if req.hardcopy_requested == True:
                    req.verified = True
                    req.delivery_status = "0"
                    req.save()
                else:
                    req.delete()

            except Exception as e:
                # raise GraphQLError(str(e))
                print(e)
                return 'Fail'

            return 'Success'

        if int(cert_index) == 1:
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
                if req.hardcopy_requested == True:
                    req.verified = True
                    req.delivery_status = "0"
                    req.save()
                else:
                    req.delete()
            except Exception as e:
                return str(e)

            return 'Success'

        if int(cert_index) == 4:
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
                if req.hardcopy_requested == True:
                    req.verified = True
                    req.delivery_status = "0"
                    req.save()
                else:
                    req.delete()
            except Exception as e:
                # raise GraphQLError(str(e))
                print(e)
                return 'Fail'

            return 'Success'

        return "Error"

    def resolve_delete_request(self, info, id, remarks=None):

        certificate_choices = [
            "Semester Certificate",
            "Migration Certificate",
            "Domicile Certificate",
            "Affadavit",
            "Character Certificate",
        ]
        usr = info.context.user

        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        teacher = Teacher.objects.get(user=usr)
        if teacher == None:
            raise GraphQLError('Not a valid teacher')

        req = Certificate_Request.objects.get(id=id)

        if req == None:
            raise GraphQLError('Not a valid Request')
        reqIndex = int(req.certificate_status)
        cert_name = certificate_choices[reqIndex]
        student = req.student
        req.delete()
        mail = EmailMessage(f"Request Rejected",
                            f"Your Request for {cert_name} Certificate has been rejected by the Institute",
                            EMAIL_HOST_USER,
                            [student.email])
        mail.send()

        return "Success"

    def resolve_student_delete_request(self, info):
        usr = info.context.user

        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        student = Student.objects.get(user=usr)
        if student == None:
            raise GraphQLError('Not a valid Student')

        req = Certificate_Request.objects.get(id=id)

        if req == None:
            raise GraphQLError('Not a valid Request')

        req.delete()

        return "Success"

    def resolve_get_all_request(self, info):
        usr = info.context.user

        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        teacher = Teacher.objects.get(user=usr)
        if teacher == None:
            raise GraphQLError('Not a valid teacher')

        l = Certificate_Request.objects.filter(
            student__institute=teacher.institute).filter(delivery_done=False)

        return l

    def resolve_get_manager_request(self, info):
        usr = info.context.user

        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        manager = Manager.objects.get(user=usr)
        if manager == None:
            raise GraphQLError('Not a valid Manager')

        l = Certificate_Request.objects.filter(
            verified=True).filter(delivery_done=False)

        return l

    def resolve_get_all_manager(self, info):
        usr = info.context.user

        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        teacher = Teacher.objects.get(user=usr)
        if teacher == None:
            raise GraphQLError('Not a valid teacher')

        manager_list = Manager.objects.all()

        return manager_list

    def resolve_get_all_sem_subjects_for_students(self, info, sem, degree, graduating_year):

        usr = info.context.user

        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        student = Student.objects.get(user=usr)
        if student == None:
            raise GraphQLError('Not a valid student!')

        subjects = Semester_Subject_Registration.objects.filter(institute=student.institute).filter(
            graduating_year=graduating_year).filter(semester=sem).filter(degree=degree)

        return subjects

    def resolve_get_all_sem_grades_for_students(self, info, sem):
        usr = info.context.user

        if usr.is_anonymous:
            raise GraphQLError('Not logged in!')

        student = Student.objects.get(user=usr)
        if student == None:
            raise GraphQLError('Not a valid student!')

        grades = Academic_Record.objects.filter(
            institute=student.institute).filter(semester=sem)

        return grades
