from django.shortcuts import render
from.models import Contact

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def education(request):
    return render(request,'education.html')

def projects(request):
    return render(request,'projects.html')

def contact(request):
    return render(request,'contact.html')

def savecont(request):
    
    if request.method == 'POST':
        name = request.POST.get('NAME')
        email = request.POST.get('EMAIL')
        subject = request.POST.get('SUBJECT')
        message = request.POST.get('MESSAGE')
        print(name)
        Contact.objects.create(name=name,email=email,message=message,subject=subject)
        
        return render(request,'home.html')





