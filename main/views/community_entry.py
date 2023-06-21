from django.shortcuts import render, redirect
from main.models import Professional
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
import random


import random
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.models import Professional

@login_required
def request_community_entry(request):
    profession_choices = Professional.PROFESSION_CHOICES 
    if request.method == 'POST':
        profession = request.POST.get('profession')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        user_input = request.POST.get('user_input')

        # Check if user entered a new profession
        if user_input:
            existing_categories = [choice[0] for choice in Professional.PROFESSION_CHOICES]

            if user_input not in existing_categories:
                new_choice = (user_input, user_input.capitalize())
                Professional.PROFESSION_CHOICES.append(new_choice)

        user = request.user

        try:
            professional = Professional.objects.get(user=user)
            # A Professional instance already exists for the user
            professional.address = address
            professional.phone_number = phone_number
            professional.profession = profession
            professional.ref_num = random.randint(1000, 9999)
            professional.save()
        except Professional.DoesNotExist:
            # No Professional instance exists for the user, create a new one
            Professional.objects.create(user=user, address=address, phone_number=phone_number, profession=profession, ref_num=random.randint(1000, 9999))

        return redirect('community_entry_success')  # Redirect to a success page

    professionals = Professional.objects.all()
    return render(request, 'request_community_entry.html', {'professionals': professionals})


@login_required
def verify_community_member(request, profession, user_id):
    if request.method == 'POST':
        # Assuming you have a form to verify the member with a submit button

        # Retrieve the specific profession model instance based on the profession name
        member = get_object_or_404(Professional, user_id=user_id, profession=profession)
        member.is_verified = True
        member.save()

        # Redirect to a success page or perform any other desired actions

    # Render the verification form or template
    return render(request, 'verify_community_member.html')


@login_required
def community_entry_success(request):
    return render(request, 'community_entry_success.html')
