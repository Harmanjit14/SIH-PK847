
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
import pandas as pd
from .models import Academic_Record, Student
from .degree_data import degree_list
from django.contrib.auth.models import User


grade_credit = {
    'A': 10,
    'A-': 9,
    'B': 8,
    'B-': 7,
    'C': 6,
    'C-': 5,
    'D': 4,
    'D-': 3,
    'E': 0,
}


def render_to_pdf(template_src, location, context):
    template = get_template(template_src)
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

    try:
        with open(location, 'wb+') as output:
            pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), output)
    except Exception as e:
        print(e)
        return False

    if not pdf.err:
        return True
    return False


def get_semester_certifcate_context(student, semester):
    context = {
        'error': False,
    }
    rec = Academic_Record.objects.filter(
        student=student).filter(semester=semester)
    l = []
    context['name'] = student.first_name+student.last_name
    context['fname'] = student.father_name
    context['mname'] = student.mother_name
    context['roll'] = student.roll
    context['institute'] = student.institute.name
    context['logo'] = student.institute.logo
    context['signature'] = student.institute.signature
    context['dob'] = str(student.dob)
    context['sem'] = str(semester)
    context['degree'] = degree_list[int(student.degree)]
    context['grad'] = student.graduating_year

    total_cre = 0
    cre_grade = 0
    for r in rec:
        total_cre += r.credits
        cre_grade += (r.credits*grade_credit[r.grade])
        data = {
            'cre': r.credits,
            'subject': r.subject,
            'marks': r.marks,
            'code': r.subject_code,
            'grade': r.grade,
        }
        l.append(data)
    sgpa = cre_grade/total_cre
    context['sg'] = str(sgpa)
    context['records'] = l
    return context


def get_other_certifcates_context(student):
    context = {
        'error': False,
    }
    context['name'] = student.first_name+student.last_name
    context['fname'] = student.father_name
    context['mname'] = student.mother_name
    context['roll'] = student.roll
    context['institute'] = student.institute.name
    context['logo'] = student.institute.logo
    context['signature'] = student.institute.signature
    context['dob'] = str(student.dob)
    context['degree'] = degree_list[int(student.degree)]
    context['grad'] = student.graduating_year

    return context


def UploadStudentDataUtil(url=None, teacher=None, degree=None, graduating_year=None):
    """Get CSV of student data and add all students to DB"""
    if url == None or degree == None or teacher == None or graduating_year == None:
        return 'Error'
    df = pd.read_csv(url)
    print(df)
    # Add try catch
    institute = teacher.institute

    for i, row in df.iterrows():
        try:
            username = str(str(institute.name).replace(
                " ", "") + str(row.roll)).lower()
            usr = User(
                username=username,
                first_name=row.first_name,
                last_name=row.last_name,
                email=row.email,
            )
            usr.set_password("123456")
            usr.save()

            student = Student(
                roll=row.roll,
                first_name=row.first_name,
                last_name=row.last_name,
                email=row.email,
                institute=institute,
                mobile='+'+str(row.mobile),
                dob=str(row.dob),
                graduating_year=graduating_year,
                degree=degree,
                address=row.address,
                batch=row.batch,
                father_name=row.father_name,
                mother_name=row.mother_name,
                user=usr,
                wallet=0
            )
            student.save()
        except Exception as e:
            try:
                usr.delete()
            except Exception as f:
                print(f)
            print(e)
            return e
    return 'Done'


def UploadCSVUtil(url=None, subject=None, semester=None, batch=None, institute=None, subject_code=None, credits=None):
    """Get CSV of student marks and add student marks to DB"""
    if url == None or subject == None or semester == None or batch == None or institute == None or subject_code == None or credits == None:
        return 'Error'
    df = pd.read_csv(url)
    print(df)

    for i, row in df.iterrows():
        try:
            student = Student.objects.get(roll=row.Roll)
            obj = Academic_Record(
                semester=semester,
                institute=institute,
                subject_code=subject_code,
                student=student,
                grade=row.Grade,
                marks=row.Marks,
                subject=subject,
                graduating_year=batch,
                credits=credits)
            obj.save()
        except Exception as e:
            print(e)
            return str(e)
    return 'Done'
