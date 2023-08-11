from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
class ProfileManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super(ProfileManager, self).get_queryset(*args, **kwargs).filter()

   
    def create_professional(self, user, **kwargs):
        return self.model.objects.create(user=user, **kwargs)
    
    

class Profile(models.Model):
    boolChoice = (("M", "Male"), ("F", "Female"))
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    profile_image = models.ImageField(upload_to='media/', blank=True)
    gender = models.CharField(max_length=10, choices=boolChoice, null=True)
    birthdate = models.DateField(null=True)
    reference = models.CharField(max_length=100, default='')
    ref_num = models.IntegerField(default=None, null=True)
    Sindhi_Sub_Caste = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.user.username
    objects = ProfileManager()

    class Meta:
        abstract = True


class Professional(Profile):
    PROFESSION_CHOICES = [
    ('estate_agent', 'Estate Agent'),
    ('papad_seller', 'Papad Seller'),
    ('maharaj_swami', 'Maharaj Swami'),
    ('lada_singer', 'Lada Singer'),
    ('rasoiyo', 'Rasoiyo'),
    ('maitinwaro', 'Maitinwaro'),
    ('maitinwari', 'Maitinwari'),
    ('doctor', 'Doctor'),
    ('gynaecologist_infertility', 'Gynaecologist - Infertility Treatment'),
    ('24_hours_gynaecologist', '24 Hours Gynaecologist Doctors'),
    ('gynaecologic_oncologist', 'Gynaecologic Oncologist Doctors'),
    ('surrogacy_doctors', 'Surrogacy Doctors'),
    ('high_risk_pregnancy_doctors', 'High Risk Pregnancy Doctors'),
    ('interior_designers', 'Interior Designers'),
    ('lawyers', 'Lawyers'),
    ('neurologists', 'Neurologists'),
    ('neurosurgeons', 'Neurosurgeons'),
    ('neuro_physicians', 'Neuro Physician Doctors'),
    ('paediatric_neurologists', 'Paediatric Neurologist Doctors'),
    ('special_child_educator', 'Special Child Educator'),
    ('beauty_salons_women', 'Beauty Salons For Women'),
    ('travel_agents', 'Travel Agents'),
    ('tiffin_services', 'Tiffin Services'),
    ('tutorials', 'Tutorials'),
    ('tattoo_artists', 'Tattoo Artists'),
    ('urologists', 'Urologist Doctors'),
    ('paediatric_urologists', 'Paediatric Urologist Doctors'),
    ('urinary_tract_infection_doctors', 'Urinary Tract Infection Treatment Doctors'),
    ('work_from_home_jobs', 'Work From Home Jobs'),
    ('women_beauty_parlours', 'Women Beauty Parlours'),
    ('yoga_classes_women', 'Yoga Classes For Women'),
    ('mythology_singers', 'Mythology Singers'),
    ('classical_singers', 'Classical Singers'),
    ('pop_singers', 'Pop Singers'),
    ('online_shopping', 'Online Shopping'),
    ('real_diamond_jewellery', 'Real Diamond Jewellery'),
    ('imitation_jewellery', 'Imitation Jewellery'),
    ('entrepreneur', 'Entrepreneur')

    ]

    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    profession = models.CharField(max_length=50, choices=PROFESSION_CHOICES, blank=True, null=True)
    desc = models.TextField(max_length=500, default='')
    is_verified = models.BooleanField(default=False)

    def get_profession_choices(self):
        choices = self.PROFESSION_CHOICES.copy()
        if self.profession and (self.profession, self.profession) not in choices:
            choices.append((self.profession, self.profession))
        return choices

    def __str__(self):
        return self.user.username

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class VerifiedProfessionalAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone_number', 'profession', 'is_verified')
    list_filter = ('is_verified',)
    search_fields = ('user__username', 'address', 'phone_number')
    list_per_page = 20


class NonVerifiedProfessionalAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone_number', 'profession', 'is_verified')
    list_filter = ('is_verified',)
    search_fields = ('user__username', 'address', 'phone_number')
    list_per_page = 20
