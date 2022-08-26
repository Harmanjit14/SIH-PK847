from twilio.twiml.voice_response import VoiceResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .degree_data import degree_choices
from django.urls import reverse
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
            'code': r.subject_code,
            'grade': r.grade,
        }
        l.append(data)
    context['records'] = l
    print(context)
    return render(request, 'certificate.html', context=context)


@csrf_exempt
def answer(request: HttpRequest) -> HttpRequest:
    vr = VoiceResponse()
    vr.say('Hello!, Welcome to FridayNights. Your responses are being recorded. What academic certificate do you wish to be delivered')
    # with vr.gather(
    #     action=voice_actions(vr, request),
    #     finish_on_key='#',
    #     timeout=20,
    # ) as gather:
    #     gather.say(
    #         'Please press 1 for hindi and 2 for English and press # to end.')
    
    # vr.say("Thank You")
    
    return HttpResponse(str(vr), content_type='text/xml')


def voice_actions(vr, request):
    val = request.POST.get('Digits')
    for d in val:
        if d == 1:
            vr.say("HINDI")
        elif d == 2:
            vr.say("ENGLISH")
        else:
            vr.say("AGAIN")
            vr.redirect('answer')
    return
