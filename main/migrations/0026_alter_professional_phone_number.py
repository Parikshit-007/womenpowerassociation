# Generated by Django 4.1.3 on 2023-06-28 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_professional_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
