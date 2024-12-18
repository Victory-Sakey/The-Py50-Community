# Generated by Django 4.2.7 on 2024-11-17 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Onboarding', '0004_alter_scholarregistrationmodel_email_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarregistrationmodel',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('Rather not say', 'Rather not say')], default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='scholarregistrationmodel',
            name='payment_plan',
            field=models.IntegerField(choices=[(6000, 'Half-Payment (₦6,000)'), (12000, 'Full-Payment (₦12,000)')], default=None),
        ),
    ]
