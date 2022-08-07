from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
import pandas as pd
from .models import Academic_Record, Institute, Student
from .degree_data import degree_choices


def UploadPDF(url=None, subject=None, semester=None, batch=None, institute_id=None):
    if url == None or subject == None or semester == None or batch == None or institute_id == None:
        return 'Error'
    df = pd.read_csv(url)
    print(df)
    # Add try catch
    institute = Institute.objects.get(id=institute_id)

    for i, row in df.iterrows():
        try:
            student = Student.objects.get(roll=row.Roll)
            obj = Academic_Record.objects.create(
                semester=semester, institute=institute, student=student, grade=row.Grade, marks=row.Marks, subject=subject, batch=batch)
            obj.save()
        except:
            continue
    return 'Done'


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
    context['name'] = student.name
    context['roll'] = student.roll
    context['institute'] = student.institute.name
    context['logo'] = student.institute.logo
    context['signature'] = student.institute.signature
    context['dob'] = str(student.dob)
    context['sem'] = str(semester)
    context['degree'] = list(degree_choices)[int(student.degree)][1]
    for r in rec:
        data = {
            'subject': r.subject,
            'marks': r.marks,
            'code': r.subject_code,
            'grade': r.grade,
        }
        l.append(data)
    context['records'] = l
    return context
