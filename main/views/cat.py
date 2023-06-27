from django.shortcuts import redirect, render
from main.models import Professional
from datetime import date

def professionals_by_profession(request, profession):
    professionals = Professional.objects.filter(profession=profession, is_verified=True)
    template_name = f'{profession}.html'
    context = {'professionals': professionals}
    return render(request, template_name, context)


def separate_profession(request, profession):
    if profession == 'estate_agent':
        agents = Professional.objects.filter(profession='estate_agent', is_verified=True)
        verified_count = agents.count()
        return render(request, 'estate_agents.html', {'agents': agents, 'current_date': date.today(), 'verified_count': verified_count})
    elif profession == 'papad_seller':
        sellers = Professional.objects.filter(profession='papad_seller', is_verified=True)
        verified_count = sellers.count()
        return render(request, 'papad_sellers.html', {'sellers': sellers, 'verified_count': verified_count})
    elif profession == 'maharaj_swami':
        swamis = Professional.objects.filter(profession='maharaj_swami', is_verified=True)
        verified_count = swamis.count()
        return render(request, 'maharaj_swamis.html', {'swamis': swamis, 'current_date': date.today(),'verified_count': verified_count})
    elif profession == 'lada_singer':
        singers = Professional.objects.filter(profession='lada_singer', is_verified=True)
        verified_count = singers.count()
        return render(request, 'lada_singers.html', {'singers': singers,'current_date': date.today(), 'verified_count': verified_count})
    elif profession == 'rasoiyo':
        rasoiyos = Professional.objects.filter(profession='rasoiyo', is_verified=True)
        verified_count = rasoiyos.count()
        return render(request, 'rasoiyos.html', {'rasoiyos': rasoiyos, 'current_date': date.today(),'verified_count': verified_count})
    elif profession == 'maitinwaro':
        maitinwaros = Professional.objects.filter(profession='maitinwaro', is_verified=True)
        verified_count = maitinwaros.count()
        return render(request, 'maitinwaros.html', {'maitinwaros': maitinwaros, 'current_date': date.today(),'verified_count': verified_count})
    elif profession == 'maitinwari':
        maitinwaris = Professional.objects.filter(profession='maitinwari', is_verified=True)
        verified_count = maitinwaris.count()
        return render(request, 'maitinwaris.html', {'maitinwaris': maitinwaris,'current_date': date.today(), 'verified_count': verified_count})
    elif profession == 'doctor':
        doctors = Professional.objects.filter(profession='doctor', is_verified=True)
        verified_count = doctors.count()
        return render(request, 'doctors.html', {'doctors': doctors, 'current_date': date.today(), 'verified_count': verified_count})
    elif profession == 'engineer':
        engineers = Professional.objects.filter(profession='engineer', is_verified=True)
        verified_count = engineers.count()
        return render(request, 'engineers.html', {'engineers': engineers, 'current_date': date.today(), 'verified_count': verified_count})
    elif profession == 'genuine properties':
        genuine_properties = Professional.objects.filter(profession='genuine properties', is_verified=True)
        verified_count = genuine_properties.count()
        return render(request, 'genuine_properties.html', {'genuine_properties': genuine_properties, 'current_date': date.today(), 'verified_count': verified_count})
    elif profession == 'safe tourism':
        safe_tourism = Professional.objects.filter(profession='safe tourism', is_verified=True)
        verified_count = safe_tourism.count()
        return render(request, 'safe_tourism.html', {'safe_tourism': safe_tourism, 'current_date': date.today(), 'verified_count': verified_count})
    elif profession == 'social workers':
        social_workers = Professional.objects.filter(profession='social workers', is_verified=True)
        verified_count = social_workers.count()
        return render(request, 'social_workers.html', {'social_workers': social_workers, 'current_date': date.today(), 'verified_count': verified_count})
    elif profession == 'education':
        education = Professional.objects.filter(profession='education', is_verified=True)
        verified_count = education.count()
        return render(request, 'education.html', {'education': education, 'current_date': date.today(), 'verified_count': verified_count})
    elif profession == 'food industries':
        food_industries = Professional.objects.filter(profession='food industries', is_verified=True)
        verified_count = food_industries.count()
        return render(request, 'food_industries.html', {'food_industries': food_industries, 'current_date': date.today(), 'verified_count': verified_count})
    elif profession == 'advocates':
        advocates = Professional.objects.filter(profession='advocates', is_verified=True)
        verified_count = advocates.count()
        return render(request, 'advocates.html', {'advocates': advocates, 'current_date': date.today(), 'verified_count': verified_count})
    elif profession == 'entrepreneur':
        entrepreneur= Professional.objects.filter(profession='entrepreneur', is_verified=True)
        verified_count = advocates.count()
        return render(request, 'entrepreneur.html', {'entrepreneur': entrepreneur, 'current_date': date.today(), 'verified_count': verified_count})
    else:
        # Handle the case when an invalid profession is selected
        return redirect('home')  # Redirect to the home page or any other desired page
