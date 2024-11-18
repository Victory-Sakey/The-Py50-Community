from django import forms
from .models import ScholarRegistrationModel

class ScholarRegistrationForm(forms.ModelForm):
    class Meta:
        model = ScholarRegistrationModel
        exclude = ['date_joined']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 p-2 poppins-medium placeholder:text-gray-400 focus:outline-none sm:text-sm/6' , 'placeholder': 'Your First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 p-2 poppins-medium placeholder:text-gray-400 focus:outline-none sm:text-sm/6' , 'placeholder': 'Your Last Name'}),
            'email_address': forms.EmailInput(attrs={'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 p-2 poppins-medium placeholder:text-gray-400 focus:outline-none sm:text-sm/6' , 'placeholder': 'Enter your Email Address'}),
            'phone_number': forms.TextInput(attrs={'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 p-2 poppins-medium placeholder:text-gray-400 focus:outline-none sm:text-sm/6' , 'placeholder': '+234...'}),
            'gender': forms.RadioSelect(attrs={'class': 'sm:text-sm/6 py-2 poppins-medium text-gray-700'}),
            'country': forms.TextInput(attrs={'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 p-2 poppins-medium placeholder:text-gray-400 focus:outline-none sm:text-sm/6' , 'placeholder': 'Enter your Country here'}),
            'city': forms.TextInput(attrs={'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 p-2 poppins-medium placeholder:text-gray-400 focus:outline-none sm:text-sm/6' , 'placeholder': 'Enter your City here'}),
            'about': forms.Textarea(attrs={'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 p-2 poppins-medium placeholder:text-gray-400 focus:outline-none sm:text-sm/6'}),
            'expectations': forms.Textarea(attrs={'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 p-2 poppins-medium placeholder:text-gray-400 focus:outline-none sm:text-sm/6' ,}),
            'how_did_you_hear': forms.Textarea(attrs={'class': 'block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 p-2 poppins-medium placeholder:text-gray-400 focus:outline-none sm:text-sm/6' , 'placeholder': 'How did you hear about Py50  e.g: Facebook, Flyer, e.t.c'}),
            'payment_plan': forms.RadioSelect(attrs={'class': 'sm:text-sm/6 py-2 poppins-medium text-gray-700'}),
        }