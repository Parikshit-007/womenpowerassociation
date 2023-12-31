# Generated by Django 4.1.3 on 2023-08-11 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='profession',
            field=models.CharField(blank=True, choices=[('estate_agent', 'Estate Agent'), ('papad_seller', 'Papad Seller'), ('maharaj_swami', 'Maharaj Swami'), ('lada_singer', 'Lada Singer'), ('rasoiyo', 'Rasoiyo'), ('maitinwaro', 'Maitinwaro'), ('maitinwari', 'Maitinwari'), ('doctor', 'Doctor'), ('gynaecologist_infertility', 'Gynaecologist - Infertility Treatment'), ('24_hours_gynaecologist', '24 Hours Gynaecologist Doctors'), ('gynaecologic_oncologist', 'Gynaecologic Oncologist Doctors'), ('surrogacy_doctors', 'Surrogacy Doctors'), ('high_risk_pregnancy_doctors', 'High Risk Pregnancy Doctors'), ('interior_designers', 'Interior Designers'), ('lawyers', 'Lawyers'), ('neurologists', 'Neurologists'), ('neurosurgeons', 'Neurosurgeons'), ('neuro_physicians', 'Neuro Physician Doctors'), ('paediatric_neurologists', 'Paediatric Neurologist Doctors'), ('special_child_educator', 'Special Child Educator'), ('beauty_salons_women', 'Beauty Salons For Women'), ('travel_agents', 'Travel Agents'), ('tiffin_services', 'Tiffin Services'), ('tutorials', 'Tutorials'), ('tattoo_artists', 'Tattoo Artists'), ('urologists', 'Urologist Doctors'), ('paediatric_urologists', 'Paediatric Urologist Doctors'), ('urinary_tract_infection_doctors', 'Urinary Tract Infection Treatment Doctors'), ('work_from_home_jobs', 'Work From Home Jobs'), ('women_beauty_parlours', 'Women Beauty Parlours'), ('yoga_classes_women', 'Yoga Classes For Women'), ('mythology_singers', 'Mythology Singers'), ('classical_singers', 'Classical Singers'), ('pop_singers', 'Pop Singers'), ('online_shopping', 'Online Shopping'), ('real_diamond_jewellery', 'Real Diamond Jewellery'), ('imitation_jewellery', 'Imitation Jewellery'), ('entrepreneur', 'Entrepreneur')], max_length=50, null=True),
        ),
    ]
