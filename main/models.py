from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
class ProfileManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super(ProfileManager, self).get_queryset(*args, **kwargs).filter()

    def create(self, *args, **kwargs):
        raise NotImplementedError("You cannot create Profile objects directly. Use a subclass instead.")


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
        ('engineer', 'Engineer'),
        ('genuine_properties', 'Genuine Properties'),
        ('safe_tourism', 'Safe Tourism'),
        ('social_workers', 'Social Workers'),
        ('education', 'Education'),
        ('food_industries', 'Food Industries'),
        ('advocates', 'Advocates'),
        ('entrepreneur', 'Entrepreneur'),
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
