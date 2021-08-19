from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    if request.method == 'POST':
        email = request.POST.get('email', 'test@email.com')
        f_name = request.POST.get('f_name', '')
        l_name = request.POST.get('l_name', '')
        messages.success(request, f'Thank you {f_name} {l_name} for your message. Check your email for our response')
        subject = "KoredeDavid!!! Portfolio: Zuri Task"
        body = f'Thank you {f_name} {l_name} for your response'
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [email])
        return redirect('home')
    return render(request, 'resume/index.html')
