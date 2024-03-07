# forms.py
from django import forms
from .models import Utilisateur
from django.forms import ModelForm
from . import models
# listings/forms.py

class UtilisateurForm(ModelForm):
   class Meta:
      model = Utilisateur
      fields = {'nom', 'mail', 'message',}
   