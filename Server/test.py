# import pandas as pd
# url = "https://firebasestorage.googleapis.com/v0/b/stately-pulsar-343510.appspot.com/o/static%2Ftest.csv?alt=media&token=25adb90b-5266-4304-89a8-66c501c9733a"

# df = pd.read_csv(url)
# print(df)
#from django.shortcuts import render
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
#from .models import Academic_Record



# Create your views here.
def generate_pdf(request):
    buf=io.BytesIO()
    c= canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Halvetica",14)
    #add somelines
    lines=[]
    #records=Academic_Record.objects.all()

    # for record in records:
    #     lines.append(record.id)
    #     lines.append(record.semester)
    #     lines.append(record.institute)
    #     lines.append(record.student)
    #     lines.append(record.subject)
    #     lines.append(record.grade)
    #     lines.append(record.marks)
    #     lines.append("===========================")
    #lines = [
        "this is 1"
        "this is 2"
    #]
    lines.append("1")
    lines.append("5")
    lines.append("tiet")
    lines.append("ballooo")
    lines.append("maths")
    lines.append("A")
    lines.append("87")
    lines.append("===========================")

    for line in lines:

        textob.textline(line)
    
    c.drawText(textob)
    c.showPage()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename="certificates")