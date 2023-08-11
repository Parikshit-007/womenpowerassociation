from django.shortcuts import redirect, render
from main.models import Professional
from datetime import date

def professionals_by_profession(request, profession):
    professionals = Professional.objects.filter(profession=profession, is_verified=True)
    template_name = f'{profession}.html'
    context = {'professionals': professionals}
    return render(request, template_name, context)


def separate_profession(request, profession):
    professions_with_views = {
        'estate_agent': {'template': 'estate_agents.html'},
        'papad_seller': {'template': 'papad_sellers.html'},
        'maharaj_swami': {'template': 'maharaj_swamis.html'},
        'lada_singer': {'template': 'lada_singers.html'},
        'rasoiyo': {'template': 'rasoiyos.html'},
        'maitinwari': {'template': 'maitinwaris.html'},
        'doctor': {'template': 'doctors.html'},
        'engineer': {'template': 'engineers.html'},
        'genuine_properties': {'template': 'genuine_properties.html'},
        'safe_tourism': {'template': 'safe_tourism.html'},
        'social_workers': {'template': 'social_workers.html'},
        'education': {'template': 'education.html'},
        'food_industries': {'template': 'food_industries.html'},
        'advocates': {'template': 'advocates.html'},
        'entrepreneur': {'template': 'entrepreneur.html'},
        'astrologer': {'template': 'astrologers.html'},
        'life_coach': {'template': 'life_coaches.html'},
        'car_rental': {'template': 'car_rentals.html'},
        'dentist': {'template': 'dentists.html'},
        'gynaecologist_obstetrician': {'template': 'gynaecologists_obstetricians.html'},
        'gynaecologist_infertility':{'template': 'gynaecologist_infertility.html'}
        # Add more professions here
    }



    if profession in professions_with_views:
        profession_data = professions_with_views[profession]
        professionals = Professional.objects.filter(profession=profession, is_verified=True)
        verified_count = professionals.count()
        template = profession_data['template']
        
        profession_name = profession.replace("_", " ").capitalize()  # Convert profession name to a readable format
        result_count = f"{verified_count} Results on {date.today()}"
        
        context = {
            'professionals': professionals,
            'current_date': date.today(),
            'verified_count': verified_count,
            'profession_name': profession_name,
            'result_count': result_count,
        }
        
        return render(request, template, context)
    else:
        # Handle the case when an invalid profession is selected
        return redirect('home')  # Redirect to the home page or any other desired page

