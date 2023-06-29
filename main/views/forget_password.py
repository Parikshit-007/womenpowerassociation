from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import random

from main.models import Profile, Professional

# Forget Password View
def forget_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            profile = Professional.objects.get(user=user)
            otp = random.randint(100000, 999999)
            profile.otp = otp
            profile.save()
            subject = 'Reset your password'
            message = f'Your OTP for resetting your password is {otp}.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, 'OTP has been sent to your email.')
            return redirect('verify_otp', email=email)
        except User.DoesNotExist:
            messages.error(request, 'Email does not exist.')
    return render(request, 'forget_password.html')


# Verify OTP View
def verify_otp(request, email):
    if request.method == 'POST':
        otp = request.POST['otp']
        try:
            user = User.objects.get(email=email)
            profile = Professional.objects.get(user=user)
            if profile.otp == otp:
                return redirect('reset_password', email=email)
            else:
                messages.error(request, 'Invalid OTP.')
        except User.DoesNotExist:
            messages.error(request, 'Email does not exist.')
    return render(request, 'verify_otp.html', {'email': email})


# Reset Password View
def reset_password(request, email):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            try:
                user = User.objects.get(email=email)
                profile = Professional.objects.get(user=user)
                user.set_password(password)
                profile.otp = None
                profile.save()
                user.save()
                messages.success(request, 'Password reset successfully. Please login.')
                return redirect('login')
            except User.DoesNotExist:
                messages.error(request, 'Email does not exist.')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'reset_password.html', {'email': email})
