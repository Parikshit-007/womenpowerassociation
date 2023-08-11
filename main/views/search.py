from django.shortcuts import render
from django.db.models import Q
from main.models import Professional
from django.shortcuts import render
from django.db.models import Q
from main.models import Professional
from datetime import date

def search(request):
    query = request.GET.get('q', '')
    name_results = request.GET.get('name_results', '')
    profession_results = request.GET.get('profession_results', '')
    address_results = request.GET.get('address_results', '')

    professionals = Professional.objects.filter(
        Q(user__username__icontains=name_results) &
        (Q(address__icontains=address_results) & Q(profession__iexact=profession_results))
    )

    for professional in professionals:
        if not professional.profile_image:
            professional.profile_image = 'path/to/default/image.jpg'

    category_name = request.GET.get('category_name', 'All Categories')  # Default value if not provided
    verified_count = professionals.count()
    result_count = f"{verified_count} Results on {date.today().strftime('%d %B, %Y')}"


    context = {
        'query': query,
        'name_results': name_results,
        'profession_results': profession_results,
        'address_results': address_results,
        'professionals': professionals,
        'category_name': category_name,
        'result_count': result_count,
    }

    return render(request, 'search.html', context)



