from django.shortcuts import render,redirect
from .models import*
from .forms import*


# Create your views here.
def profil(request):
	text = "mon profile"
	return render(request,'profile.html',locals())

def auteur(request):
	auteur_form = AuteurForms(request.POST or None)
	if(request.method == 'POST'):
		if(auteur_form.is_valid()):
			auteur_form.save()
	auteur_form = AuteurForms()
	return render(request,"forms.html",locals())

def emplacement(request):
	emplacement_form = EmplacementForms(request.POST or None)
	if(request.method == 'POST'):
		if(emplacement_form.is_valid()):
			emplacement_form.save()
	emplacement_form = EmplacementForms()
	return render(request,"forms.html",locals())

def livre(request):
	livre_form = LivreForms(request.POST or None)
	if(request.method == 'POST'):
		if(livre_form.is_valid()):
			livre_form.save()
			return redirect('listeL')
	livre_form = LivreForms()
	return render(request,"forms.html",locals())

def lecteur(request):
	lecteur_form = LecteurForms(request.POST or None)
	if(request.method == 'POST'):
		if(lecteur_form.is_valid()):
			lecteur_form.save()
	lecteur_form = LecteurForms()
	return render(request,"forms.html",locals())

def listes(request):
	liste_form=True
	ibitabu = Livre.objects.all()
	return render(request, "listes.html", locals())

def modifier_livre(request,id):
	book = Livre.objects.get(id=id)
	modifier_forms = LivreForms(request.POST or None,instance=book)

	if(request.method == 'POST'):
		if(modifier_forms.is_valid()):
			modifier_forms.save()
			return redirect('listeL')		
	modifier_forms = LivreForms(instance=book)
	return render(request, "forms.html", locals())

def delete_livre(request,id):
	book= Livre.objects.get(id=id)
	book.delete()
	return redirect('listeL')








