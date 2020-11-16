from django.shortcuts import render
from .models import*
from .forms import*

# Create your views here.
def profil(request):
	text = "mon profile"
	return render(request,'profile.html',locals())

def Emplacement(request):

	emplacement_form = EmplacementForms(request.POST or None)
	if(request.method == 'POST'):
		if(emplacement_form.is_valid()):
			emplacement_form.save()
	emplacement_form = EmplacementForms()
	return render(request,"forms.html",locals())






