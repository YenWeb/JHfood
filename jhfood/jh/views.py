from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm
# Create your views here.
def index(request):
    return render(request,'index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Envoyer l'email
            send_mail(
                'Message de contact',
                f'Nom: {nom}\nEmail: {email}\n\n{message}',
                'votre@email.com',
                ['udjineyenchi@gmail.com'],
                fail_silently=False,
            )
            # Redirection ou affichage d'un message de succès
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
    