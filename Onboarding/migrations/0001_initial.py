# Generated by Django 4.2.7 on 2024-11-17 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScholarRegistrationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email_address', models.EmailField(error_messages={'unique': 'This email has ben registered'}, max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('Prefer not to say', 'Prefer not to say')], default='Male', max_length=255)),
                ('country', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('about', models.TextField(error_messages={'max_length': 'Must not be more than 5000 words'}, max_length=5000)),
                ('expectations', models.TextField(error_messages={'max_length': 'Must not be more than 5000 words'}, max_length=5000)),
                ('how_did_you_hear', models.TextField(error_messages={'max_length': 'Must not be more than 5000 words'}, max_length=5000)),
                ('payment_plan', models.CharField(choices=[(6000.0, 'Half-Payment (₦6,000)'), (12000.0, 'Full-Payment (₦12,000)')], default='Half-Payment (₦6,000)', max_length=255)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]