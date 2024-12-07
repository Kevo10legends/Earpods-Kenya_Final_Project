# Generated by Django 5.0.2 on 2024-12-06 05:54

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LatestBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('image', models.ImageField(upload_to='uploads/products/')),
            ],
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('description', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('image', models.ImageField(upload_to='uploads/products/')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='javaecomapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('description', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('image', models.ImageField(upload_to='uploads/products/')),
                ('is_sale', models.BooleanField(default=False)),
                ('sale_price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='javaecomapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('address', models.CharField(default='', max_length=250)),
                ('phone', models.CharField(max_length=10)),
                ('date_ordered', models.DateField(default=datetime.datetime.today)),
                ('status', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='javaecomapp.customer')),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='javaecomapp.product')),
            ],
        ),
    ]
