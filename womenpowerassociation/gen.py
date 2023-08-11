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
from main.models import Profile, Professional

# Rest of your code
import pandas as pd
from django.contrib.auth.models import User
from main.models import Profile, Professional
def generate_excel_table():
    # Query all Professional objects
    professionals = Professional.objects.select_related('user')

    # Create a DataFrame to hold the data
    data = {
        'First Name': [professional.user.first_name for professional in professionals],
        'Last Name': [professional.user.last_name for professional in professionals],
        'Profile Image':[professional.profile_image for professional in professionals],
        'Email': [professional.user.email for professional in professionals],
        'Username': [professional.user.username for professional in professionals],
        'Password': [professional.user.password for professional in professionals],
        'Address': [professional.address for professional in professionals],
        'Phone Number': [professional.phone_number for professional in professionals],
        'Gender': [professional.gender for professional in professionals],
        'Birthdate': [professional.birthdate for professional in professionals],
        'Reference': [professional.reference for professional in professionals],
        'Ref Num': [professional.ref_num for professional in professionals],
        'Sindhi Sub Caste': [professional.Sindhi_Sub_Caste for professional in professionals],
        'Profession': [professional.profession for professional in professionals],
        'Description': [professional.desc for professional in professionals],
        'Is Verified': [professional.is_verified for professional in professionals]
    }
    df = pd.DataFrame(data)

    # Save the DataFrame to an Excel file
    file_path = 'professionals.xlsx'
    df.to_excel(file_path, index=False)
    print(f"Excel table saved to: {file_path}")

# Usage examples
generate_excel_table()
