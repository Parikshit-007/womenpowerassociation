# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import random

# Forget Password View
def forget_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            otp = random.randint(100000, 999999)
            user.profile.otp = otp
            user.profile.save()
            subject = 'Reset your password'
            message = f'Your OTP for resetting your password is {otp}.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, 'OTP has been sent to your email.')
            return redirect('verify_otp', email=email)
        else:
            messages.error(request, 'Email does not exist.')
    return render(request, 'forget_password.html')


# Verify OTP View
def verify_otp(request, email):
    if request.method == 'POST':
        otp = request.POST['otp']
        if User.objects.filter(email=email, profile__otp=otp).exists():
            return redirect('reset_password', email=email)
        else:
            messages.error(request, 'Invalid OTP.')
    return render(request, 'verify_otp.html', {'email': email})


# Reset Password View
def reset_password(request, email):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            user = User.objects.get(email=email)
            user.set_password(password)
            user.profile.otp = None
            user.profile.save()
            user.save()
            messages.success(request, 'Password reset successfully. Please login.')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'reset_password.html', {'email': email})
