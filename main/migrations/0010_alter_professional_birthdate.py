# Generated by Django 4.1.3 on 2023-05-19 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_professional_sindhi_sub_caste_professional_birthdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='birthdate',
            field=models.DateField(null=True),
        ),
    ]