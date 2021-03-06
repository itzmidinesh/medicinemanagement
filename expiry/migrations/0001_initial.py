# Generated by Django 3.1.1 on 2020-09-25 06:33

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=100, unique=True)),
                ('shop_address', models.CharField(max_length=500)),
                ('shop_area', models.CharField(max_length=30)),
                ('shop_locality', models.CharField(max_length=30)),
                ('mobile_number', models.CharField(blank=True, max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message="Entered mobile number isn't in a right format!", regex='^[0-9]{10}$')])),
                ('license1', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message="Entered license number isn't in a right format!", regex='^[A-Z]{3}\\/[\\d]{4}\\/[\\d]{2}$')])),
                ('license2', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message="Entered license number isn't in a right format!", regex='^[A-Z]{3}\\/[\\d]{4}\\/[\\d]{2}$')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=50)),
                ('expiry_date', models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date.today)])),
                ('medicine_per_strip', models.DecimalField(decimal_places=0, max_digits=5, validators=[django.core.validators.MinValueValidator(1)])),
                ('medicine_mrp', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('medicine_quantity', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)])),
                ('medicine_added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicines', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
