from django.shortcuts import get_object_or_404, render
from main.models import Profile, Professional, Contact

# Create your views here.

def home(request):
   
    
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')
def contactus(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'contactus.html', {'thank': thank})

def terms_condition(request):
    return render(request, 'terms-condition')

from django.shortcuts import get_object_or_404, render
from main.models import Profile, Professional

def FullView(request, id):
    professional = get_object_or_404(Professional, id=id)
  #  profile = get_object_or_404(Profile, id=id)
    return render(request, 'fullview.html', {'professional': professional})#, 'profile': profile})

