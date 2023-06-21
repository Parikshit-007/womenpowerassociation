from django.shortcuts import render
from django.db.models import Q
from main.models import Professional

def search(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    name_results = request.GET.get('name_results', '')  # Get the name search query from the request
    profession_results = request.GET.get('profession_results', '')  # Get the profession search query from the request
    address_results = request.GET.get('address_results', '')  # Get the address search query from the request
    
    professionals = Professional.objects.filter(
        Q(user__username__icontains=name_results) &
        (Q(address__icontains=address_results) | Q(profession__iexact=profession_results))
    )
    
    # Check if profile_image field has a file associated with it
    for professional in professionals:
        if not professional.profile_image:
            professional.profile_image = 'path/to/default/image.jpg'  # Replace with the path to your default image file
        
    context = {
        'query': query,
        'name_results': name_results,
        'profession_results': profession_results,
        'address_results': address_results,
        'professionals': professionals
    }
    return render(request, 'search.html', context)
