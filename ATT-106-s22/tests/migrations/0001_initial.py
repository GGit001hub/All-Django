# Generated by Django 4.1.1 on 2023-02-07 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.TextField(verbose_name='Savol uchun')),
                ('v1', models.CharField(max_length=200, verbose_name='1-variant')),
                ('v2', models.CharField(max_length=200, verbose_name='2-variant')),
                ('v3', models.CharField(max_length=200, verbose_name='3-variant')),
                ('true_question', models.CharField(choices=[('v1', '<django.db.models.fields.CharField>'), ('v2', '<django.db.models.fields.CharField>'), ('v3', '<django.db.models.fields.CharField>')], max_length=200, verbose_name="To'g'ri javob")),
                ('status', models.CharField(choices=[('active', "Ko'riladigan"), ('deactive', 'Yashirish')], max_length=60, verbose_name='Holati')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
