from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact



def homepage(request):
    if request.method == 'POST':
        input_email = request.POST.get('email2')

        if input_email == '':
            messages.error(request, 'email cannot be empty')
            return redirect ('contact')
        else:
            Contact.objects.create(email = input_email)
            messages.success(request, 'Thanks for subscribing to our newsletter')
            return redirect('/')
    else:
        return render(request, 'Class/index.html')

def about(request):

    return render(request, 'Class/about.html')


def courses(request):
    
    return render(request, 'Class/courses.html')

def contact(request):
    if request.method == 'POST':
        input_name = request.POST.get('name')
        input_email = request.POST.get('email')
        input_subject = request.POST.get('subject')
        input_message = request.POST.get('message')

        if len(input_name) > 100:
            messages.error(request, 'name is too long')
            return redirect('contact')
        elif input_subject == '':
            messages.error(request, 'type cannot be empty')
            return redirect ('contact')
        elif input_email == '':
            messages.error(request, 'email cannot be empty')
            return redirect ('contact')
        elif len (input_message) > 1500:
            messages.error(request, 'message is too long')
            return redirect ('contact')
        else:
            Contact.objects.create(name=input_name, email = input_email,
                                   subject = input_subject, message = input_message)
            messages.success(request, 'Thanks for contacting us')
            return redirect('/')

    else:
        return render(request, 'Class/contact.html')

def team(request):
    
    return render(request, 'Class/team.html')

def testimonial(request):
    
    return render(request, 'Class/testimonial.html')

def error(request):
    
    return render(request, 'Class/404.html')