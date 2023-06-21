# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import random
from main.models import Profile, Professional

def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        birthdate = request.POST['birthdate']
        reference = request.POST['reference']
        ref_num = request.POST['ref_num']
        profile_image = request.FILES.get('profile_image')
        sindhi_sub_caste = request.POST['sindhi_sub_caste']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                profile = Professional.objects.create(user=user, phone_number=phone_number, gender=gender, birthdate=birthdate, reference=reference, ref_num=ref_num, profile_image=profile_image, Sindhi_Sub_Caste=sindhi_sub_caste)
                messages.success(request, 'Account created successfully. Please login.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
    
    return render(request, 'signup.html')
