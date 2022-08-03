# from django.shortcuts import render
# from django.http import FileResponse
import io

# from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
# from .models import Academic_Record



# Create your views here.
def generate_pdf():
    buf=io.BytesIO()
    c= canvas.Canvas(buf)
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    #add somelines
    lines=[]
    # records=Academic_Record.objects.all()

    lines.append('1')
    lines.append('3')
    lines.append('TIET')
    lines.append('Harman')
    lines.append('DS')
    lines.append('A')
    lines.append('90')
    lines.append("===========================")
    for line in lines:
        textob.textLine(line)
    
    c.drawText(textob)
    c.showPage()
    buf.seek(0)
    
    return FileResponse(buf, as_attachment=True, filename="certificates")

generate_pdf()