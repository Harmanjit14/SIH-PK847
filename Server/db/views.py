# from django.shortcuts import render
# from django.http import FileResponse
# import io
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter
# from .models import Academic_Record



# # # Create your views here.
# # def generate_pdf(request):
# #     buf=io.BytesIO()
# #     c= canvas.Canvas(buf, pagesize=letter, bottomup=0)
# #     textob = c.beginText()
# #     textob.setTextOrigin(inch,inch)
# #     textob.setFont("Halvetica",14)
# #     #add somelines
# #     lines=[]
# #     records=Academic_Record.objects.all()

# #     for record in records:
# #         lines.append(record.id)
# #         lines.append(record.semester)
# #         lines.append(record.institute)
# #         lines.append(record.student)
# #         lines.append(record.subject)
# #         lines.append(record.grade)
# #         lines.append(record.marks)
# #         lines.append("===========================")
# #     #lines = [
# #         "this is 1"
# #         "this is 2"
# #     #]

# #     for line in lines:
# #         textob.textline
# #         (line)
    
# #     c.drawText(textob)
# #     c.showPage()
# #     buf.seek(0)

# #     return FileResponse(buf, as_attachment=True, filename="certificates")
# from django.utils import timezone    
# from io import BytesIO
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter

# def generate_pdf(pk):
#     y = 700
#     buffer = BytesIO()
#     p = canvas.Canvas(buffer, pagesize=letter)
#     p.setFont('Helvetica', 10)
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