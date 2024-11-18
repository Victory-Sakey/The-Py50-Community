from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render , redirect
from .models import ScholarRegistrationModel
from .forms import ScholarRegistrationForm
from .email_info import *


def Onboarding(request):
    return render(request, 'onboarding.html') 

def Home(request):
    return render(request , 'home.html')

def about(request):
    return render(request , 'about.html')

def join_community(request):
    return render(request , 'jc.html')

def tutor(request):
    return render(request , 'tutor.html')

def mentor(request):
    return render(request , 'mentor.html')

def scholar(request):
    return render(request , 'scholar.html')

def scholar_registration(request):
    if request.method == 'POST':
        form = ScholarRegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email_address = form.cleaned_data['email_address']
            phone_number = form.cleaned_data['phone_number']
            gender = form.cleaned_data['gender']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            about = form.cleaned_data['about']
            expectations = form.cleaned_data['expectations']
            how_did_you_hear = form.cleaned_data['how_did_you_hear']
            payment_plan = form.cleaned_data['payment_plan']

            admin_temporary_email(first_name , last_name , email_address , phone_number , gender , country , city , about , expectations , how_did_you_hear , payment_plan)

            

            form.save()


            request.session['first_name'] = first_name

            return redirect('Onboarding:payment')
        else:
            # Return the form with errors
            return render(request, 'scholar_registration.html', {'form': form})
    else:
        form = ScholarRegistrationForm()
        return render(request , 'scholar_registration.html' , {'form': form})

def admin_temporary_email(first_name , last_name , email_address , phone_number , gender , country , city , about , expectations , how , payment_plan):
    subject = f"{first_name}  just registered as a Scholar in the Py50 Community"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['emmanuelekopimo@gmail.com' , 'wisdomemmanuel20042004@gmail.com' , 'victorysakey66@gmail.com' , 'josephcosmos743@gmail.com']
    context = {'first_name': first_name , 'last_name': last_name , 'email_address': email_address , 'phone_number': phone_number , 'gender': gender , 'country': country , 'city': city , 'about': about , 'expecations': expectations , 'how': how , 'payment_plan': payment_plan} 
    
    message = render_to_string('temporary_admin_email.html', context)
    email = EmailMessage(subject, message, from_email, recipient_list)
    email.content_subtype = 'html'
    email.send(fail_silently=False)


def payment(request):
    scholar_name = request.session.get('first_name')
    context = {'scholar': scholar_name}
    return render(request , 'payment_page.html' , context)