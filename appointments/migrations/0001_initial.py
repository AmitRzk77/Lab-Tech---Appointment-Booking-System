# Generated by Django 5.2 on 2025-05-02 04:09

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('date', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('message', models.TextField(blank=True)),
                ('payment_option', models.CharField(choices=[('ONLINE PAYMENT', 'online payment'), ('PAYMENT AT CLINIC', 'payment at clinic')], max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='select_category', to='categories.category')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments_services', to='services.service')),
                ('sub_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='select_sub_category', to='categories.category')),
            ],
        ),
    ]
