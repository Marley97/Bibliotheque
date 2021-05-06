from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from datetime import datetime
from .models import*
from .forms import*


# Create your views here.
def result(request,queryset):
	obj = Livre.objects.filter(titre__contains = queryset)
	return render(request,"result.html",locals())

def profil_view(request):
	search_form = SearchForm(request.POST or None)
	if 'q' in request.GET:
		q = request.GET['q']
		livres = Livre.objects.filter(titre = q)
	else:
		livres = Livre.objects.all()
	if 's' in request.POST:
		if(search_form.is_valid()):
			s = search_form.cleaned_data['search']
			return redirect(result,s)
	return render(request,'profile.html',locals())

def action(request):
	action_form = ActionsForms(request.POST or None)
	if(action_form.is_valid()):
		exempl = action_form.save(commit=False)
		livr = Livre.objects.get(id=exempl.livre.id)
		if exempl.statut : 
			if livr.nombre_exemplaire > 0:
				livr.nombre_exemplaire-=1
				livr.save()
				exempl.save()
		else:
			livr.nombre_exemplaire+=1
			exempl.statut=False
			exempl.save()
			livr.save()
	action_form = ActionsForms()
	return render(request,"forms.html",locals())

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

def livreemprunte(request):
	emprunte_form=True
	emprunte=Actions.objects.filter(statut=True)
	return render(request,"listes.html",locals())

def livreremis(request):
	remis_form=True
	remis=Actions.objects.filter(statut=False)
	return render(request,"listes.html",locals())

def modifier_livre(request,id):
	book = Livre.objects.get(id=id)
	modifier_forms = LivreForms(request.POST or None, instance=book)

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

def registerbibliothecaire(request):
	profile_form = BibliothecaireForms(request.POST or None)
	if(request.method == 'POST'):
		if(profile_form.is_valid()):
			username=profile_form.cleaned_data['username']
			password=profile_form.cleaned_data['password'] 
			password1=profile_form.cleaned_data['password1']
			nom=profile_form.cleaned_data['nom']
			prenom=profile_form.cleaned_data['prenom']
			matricule=profile_form.cleaned_data['matricule']
			
			if(password == password1):
				user = User.objects.create_user(username = username,password = password)
				user.first_name = nom
				user.last_name = prenom
				user.save()
				profile=Bibliothecaire(user = user,matricule = matricule)
				profile.save()
				if user:
					login(request,user)
					return redirect(profil_view)
				else:
					return redirect(connexion)
			else:
				profile_form = BibliothecaireForms(request.FILES)
	profile_form = BibliothecaireForms(request.FILES)
	return render(request,'forms.html',locals())

def connexion(request):
	connexion = ConnexionForm(request.POST)
	if(request.method == 'POST'):
		if(connexion.is_valid()):
			username=connexion.cleaned_data['username']
			password=connexion.cleaned_data['password']

			user=authenticate(username = username,password = password)
			if user:
				login(request,user)
				return redirect(profil_view)
			else:
				connexion = ConnexionForm()
	connexion = ConnexionForm()
	return render(request,'forms.html',locals())

def deconnexion(request):
	logout(request)
	return redirect(connexion)







	








