from django.utils import timezone    
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def generate_pdf(pk):
    y = 700
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    # p.setFont('Helvetica', 10)
    lines=[]

    id=1234
    semester=7
    institute="TIET"
    student="Roop"
    subject="DS"
    grade="F"
    marks=99

    # lines.append(id)

    p.drawString(220, y, "PDF generate at "+timezone.now().strftime('%Y-%b-%d'))
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    return pdf
