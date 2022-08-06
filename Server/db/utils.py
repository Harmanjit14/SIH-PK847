from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
import pandas as pd
from .models import Academic_Record, Institute, Student


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


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    filename = 'certificate'
    try:
        with open(f'{filename}.pdf', 'wb+') as output:
            pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), output)
    except Exception as e:
        print(e)

    if not pdf.err:
        return True
    return False
