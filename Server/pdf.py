
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
import os
buf = io.BytesIO()
c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
lines = []
lines.append("1")
lines.append("5")
lines.append("tiet")
lines.append("ballooo")
lines.append("maths")
lines.append("A")
lines.append("87")
lines.append("===========================")

c = canvas.Canvas("hello.pdf")
#textob = c.beginText()
# textob.setTextOrigin(inch,inch)

for i, line in enumerate(lines):

    c.drawString(1 * cm, 29.7 * cm - 1 * cm - i * cm, line)

# print(textob)
# textobject = c.beginText()
# for line in multiline:
#     textobject.textLine(line)
# canvas.drawText(textobject)


#c = canvas.Canvas("hello.pdf")
# c.drawString(100,700,textob)
c.save()

os.open("hello.pdf", 34)
