from django.shortcuts import render, redirect
from main.models import EstateAgent
from django.contrib.auth.decorators import login_required

@login_required
def create_estate_agent(request):
    if request.method == 'POST':
        # Get data from user input
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')

        # Get user object associated with the current authenticated user
        user = request.user

        # Get first name, last name, email, and profile pic from user object
        first_name = user.first_name
        last_name = user.last_name
        email = user.email
        profile_pic = user.profile_pic

        # Create new EstateAgent object with user and input data
        new_estate_agent = EstateAgent(user=user, address=address, phone_number=phone_number,
                                       first_name=first_name, last_name=last_name, email=email,
                                       profile_pic=profile_pic)
        
        # Save the new object to the database
        new_estate_agent.save()

        # Redirect to success page
        return redirect('success')

    # Render the form template if the request is GET
    return render(request, 'estate_agent_form.html')
