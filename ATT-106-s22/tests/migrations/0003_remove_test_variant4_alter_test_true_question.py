# Generated by Django 4.1.1 on 2023-02-08 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_rename_v1_test_variant1_rename_v2_test_variant2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='variant4',
        ),
        migrations.AlterField(
            model_name='test',
            name='true_question',
            field=models.CharField(choices=[('variant1', '1-variant'), ('variant2', '2-variant'), ('variant3', '3-variant')], max_length=200, verbose_name="To'g'ri javob"),
        ),
    ]