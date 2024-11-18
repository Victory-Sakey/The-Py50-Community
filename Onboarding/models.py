from django.db import models

# Create your models here.
class ScholarRegistrationModel(models.Model):
    first_name = models.CharField(max_length=255 , null=False , blank=False)
    last_name = models.CharField(max_length=255 ,  null=False)
    email_address = models.EmailField(unique=True , blank=False , null=False , error_messages={
        'unique': 'The email you provided has been registered already.'
    })
    phone_number = models.CharField(max_length=255 , blank=False , null=False)
    gender = models.CharField(max_length=255 , choices=[
        ('Male' , 'Male'),
        ('Female' , 'Female'),
        ('Other' , 'Other'),
        ('Rather not say' , 'Rather not say'),
    ],
    default=None
    )
    country = models.CharField(max_length=300 , blank=False , null=False)
    city = models.CharField(max_length=300 , blank=False , null=False)
    about = models.TextField(max_length=5000 , blank=False , null=False , error_messages={
        'max_length': "Your about should not be more than 5000 words"
    })
    expectations = models.TextField(max_length=5000 , blank=False , null=False, error_messages={
        'max_length': "Your expectation should not be more than 5000 words"})
    how_did_you_hear = models.TextField(max_length=5000 , blank=False , null=False , error_messages={
        'max_length': "Must not be more than 5000 words"})
    payment_plan = models.IntegerField(choices=[
        (round(6000 , 2) , 'Half-Payment (₦6,000)'),
        (round(12000 , 2)  , 'Full-Payment (₦12,000)'),
    ] ,
    default=None
    )
    date_joined = models.DateTimeField(auto_now_add=True)


     
