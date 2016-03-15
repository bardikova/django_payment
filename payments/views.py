from django.shortcuts import render
from payments.models import Providers, Categorie

def provider_list(request):
	provider = Providers.objects.all()
	categorie = Categorie.objects.all()
	return render(request, 'providers_list.html', {
		'providers': provider, 'categorie': categorie
		})


# Create your views here.
