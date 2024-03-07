from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from .forms import UtilisateurForm
# Create your views here.
def index(request):
    return render(request,'index.html')



  # passe ce formulaire au gabarit
def success(request):
    return render(request, 'success.html')
#def success(request):
   #return HttpResponse('Success!')

def contact(request):
    submited = False
    if request.method == 'POST':
        form = UtilisateurForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
            # Envoyer l'e-mail
    else:
            form = UtilisateurForm
            if 'submitted' in request.GET:
                 submited = True
    return render(request, "index.html", {'form ': form})
            