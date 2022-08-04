from django.shortcuts import render
# # from django.http import FileResponse
# # import io
# # from reportlab.pdfgen import canvas
# # from reportlab.lib.units import inch
# # from reportlab.lib.pagesizes import letter
# from .models import Academic_Record

def certificate(request):
    return render(request,'certificate.html',context={})

# # Create your views here.
# def generate_pdf(request):
#     buf=io.BytesIO()
#     c= canvas.Canvas(buf, pagesize=letter, bottomup=0)
#     textob = c.beginText()
#     textob.setTextOrigin(inch,inch)
#     # textob.setFont("Halvetica",14)
#     #add somelines
#     lines=[]
#     records=Academic_Record.objects.all()

#     for record in records:
#         lines.append(record.id)
#         lines.append(record.semester)
#         lines.append(record.institute)
#         lines.append(record.student)
#         lines.append(record.subject)
#         lines.append(record.grade)
#         lines.append(record.marks)
#         lines.append("===========================")
#    # p.drawString(220, y, "PDF generate at "+timezone.now().strftime('%Y-%b-%d'))
#     p.showPage()
#     p.save()
#     pdf = buffer.getvalue()
#     buffer.close()
#     return pdf