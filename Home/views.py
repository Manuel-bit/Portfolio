from django.shortcuts import render, get_object_or_404
from .models import CariclumVitae

# Create your views here.

def Index(request):
    cariclumvitae = get_object_or_404(CariclumVitae)
    print(cariclumvitae.cv)
    return render(request,'Home/Index.html',{'cariclumvitae':cariclumvitae})

def Bccis(request):
    return render(request, 'Home/bccis_project.html')