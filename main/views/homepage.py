from django.shortcuts import get_object_or_404, render
from main.models import Profile, Professional

# Create your views here.

def home(request):
   
    
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def terms_condition(request):
    return render(request, 'terms-condition')

from django.shortcuts import get_object_or_404, render
from main.models import Profile, Professional

def FullView(request, id):
    professional = get_object_or_404(Professional, id=id)
  #  profile = get_object_or_404(Profile, id=id)
    return render(request, 'fullview.html', {'professional': professional})#, 'profile': profile})

