from django.shortcuts import render, get_object_or_404
from .models import CariclumVitae

# Create your views here.

def Index(request):
    cariclumvitae = get_object_or_404(CariclumVitae)
    print(cariclumvitae)
    return render(request,'Home/Index.html')