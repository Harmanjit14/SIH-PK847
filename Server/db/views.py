from django.shortcuts import render
from .degree_data import degree_choices
from .models import Academic_Record, Student

def certificate(request):
    context = {}
    s = Student.objects.get(roll=101903287)
    rec = Academic_Record.objects.filter(student=s).filter(semester=3)
    l = []
    context['name'] = s.name
    context['roll'] = s.roll
    context['institute'] = s.institute.name
    context['dob'] = str(s.dob)
    context['degree'] = list(degree_choices)[int(s.degree)][1]
    context['dob'] = str(s.dob)
    for r in rec:
        data = {
            'subject': r.subject,
            'marks': r.marks,
            'code':r.subject_code,
            'grade':r.grade,
        }
        l.append(data)
    context['records'] = l
    print(context)
    return render(request, 'certificate.html', context=context)
