# Generated by Django 4.1.3 on 2023-06-27 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_professional_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='profession',
            field=models.CharField(blank=True, choices=[('estate_agent', 'Estate Agent'), ('papad_seller', 'Papad Seller'), ('maharaj_swami', 'Maharaj Swami'), ('lada_singer', 'Lada Singer'), ('rasoiyo', 'Rasoiyo'), ('maitinwaro', 'Maitinwaro'), ('maitinwari', 'Maitinwari'), ('doctor', 'Doctor'), ('engineer', 'Engineer'), ('genuine_properties', 'Genuine Properties'), ('safe_tourism', 'Safe Tourism'), ('social_workers', 'Social Workers'), ('education', 'Education'), ('food_industries', 'Food Industries'), ('advocates', 'Advocates'), ('entrepreneur', 'Entrepreneur')], max_length=50, null=True),
        ),
    ]
