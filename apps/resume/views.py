from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.resume.models import Project

# Create your views here.
from apps.resume.serializers import MailSerializer


def index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'resume/index.html', context)


@api_view(['POST'])
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
            from_email = serializer.validated_data['from_email']
            send_mail(subject, content, from_email, receiver)
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
