import requests
import json

from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.resume.models import Project, Skill
from apps.resume.serializers import MailSerializer

# Create your views here.


def index(request):
    projects = Project.objects.all()
    skills = Skill.objects.all().order_by('rank')

    context = {
        'projects': projects,
        'skills': skills
    }
    return render(request, 'resume/index.html', context)


@api_view(['POST'])
@csrf_protect
def send_email(request):
    if request.method == 'POST':
        receiver = ['koredeoluwashola@gmail.com', ]
        serializer = MailSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            data.update(serializer.data)
            data['status'] = 'success'
            subject = f"{serializer.validated_data['name']}: {serializer.validated_data['from_email']} Portfolio"
            content = serializer.validated_data['content']
            from_email = 'KoredeDavidPortfolio@korededavid.com'
            send_mail(subject, content, from_email, receiver)
            return Response(data, status=status.HTTP_202_ACCEPTED)
        data.update(serializer.errors)
        data['status'] = 'error'
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


# This end point will not be used in this project at all but in IamAdesua Portfolio
@api_view(['POST'])
def send_grid_email(request):
    if request.method == 'POST':
        receiver = 'koredeoluwashola@gmail.com'
        serializer = MailSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            subject = f"IamAdesua🚀: Message from {serializer.validated_data['name']}"
            content = serializer.validated_data['content']
            from_email = serializer.validated_data['from_email']
            api_url = "https://api.sendinblue.com/v3/smtp/email"
            email_contents_data = {
                "sender": {
                    "name": "IamAdesua Portfolio",
                    "email": "contact@iamadesua.com"
                },
                "to": [
                    {
                        "email": receiver,
                        "name": "Adesua Iyoyojie"
                    }
                ],
                "subject": subject,
                "htmlContent": f"<html><head></head><body><p>{content}</p><br/><p>From: {from_email}</p></body></html>"
            }
            headers = {
                "Content-Type": "application/json",
                "api-key": settings.SEND_IN_BLUE_API_KEY
            }
            response = requests.post(api_url, data=json.dumps(email_contents_data), headers=headers)
            data = response.json()
            data['status'] = 'success'
            if response.status_code >= 400:
                data['status'] = 'error'
                return Response(data, status=response.status_code)
            return Response(data, status=status.HTTP_202_ACCEPTED)
        data.update(serializer.errors)
        data['status'] = 'error'
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


def contact(request, platform):
    platforms = {
        'github': 'https://github.com/KoredeDavid',
        'twitter': 'https://twitter.com/KingKoredeDavid',
        'linkedin': 'https://linkedIn.com/in/KoredeDavid',
        'whatsapp': 'https://wa.me/+2348124973682',
    }

    platform = platforms.get(platform)
    if platform is not None:
        return redirect(platform)
    else:
        raise Http404()
