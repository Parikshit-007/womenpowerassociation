import os
import sys

# Add the path to your Django project directory
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_DIR)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Jaijhulelal.settings')

import django
from django.conf import settings

django.setup()

# Rest of your code
import pandas as pd
from django.contrib.auth.models import User
from main.models import Professional


def import_data_from_excel(file_path):
    df = pd.read_excel(file_path)  # Read the Excel file into a pandas DataFrame

    for index, row in df.iterrows():
        username = row['Username']
        password = row['Password']
       # phone_number = row['Phone Number']
        profile_image = row['Profile Image']
        gender = row['Gender']
        birthdate = row['Birthdate']
        reference = row['Reference']
        ref_num = row['Ref Num']
        sindhi_sub_caste = row['Sindhi Sub Caste']
        first_name = row['First Name']
        last_name = row['Last Name']
        email = row['Email']
        address = row['Address']
        phone_number_prof = row['Phone Number']
        profession = row['Profession']
        description = row['Description']
        is_verified = row['Is Verified']
        
        try:
            # Check if a user with the given username already exists
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # Create a new User instance
            user = User(username=username, first_name=first_name, last_name=last_name, email=email)
            user.set_password(password)
            user.save()

        # Check if a Professional object already exists for the user
        if not Professional.objects.filter(user=user).exists():
            # Create a new Professional instance and associate it with the User
            professional = Professional(
                user=user,
                phone_number=phone_number_prof,
                profile_image=profile_image,
                gender=gender,
                birthdate=birthdate,
                reference=reference,
                ref_num=ref_num,
                Sindhi_Sub_Caste=sindhi_sub_caste,
                address=address,
                profession=profession,
                desc=description,
                is_verified=is_verified
            )
            # ... set other fields of the Professional model
            professional.save()

# Usage example 
"C:/User/ASUS/OneDrive/Desktop/professionals.xlsx"
file_path = 'C:/Users/ASUS/OneDrive/Desktop/professionals.xlsx'
import_data_from_excel(file_path)
