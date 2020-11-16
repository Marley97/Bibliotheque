from django import forms
from .models import *

class EmplacementForms(forms.ModelForm):

	etagere = forms.IntegerField(
		label='Etagere Numero',
		widget=forms.NumberInput(
			attrs={
				'placeholder':'Etagere numero',
				'class':'form-control'
				


				}

			))

	class Meta:
		model = Emplacement
		fields = '__all__'

class BibliothecaireForms(forms.ModelForm):

	username = forms.CharField(
		label='Nom Utilisateur',
		widget=forms.TextInput(
			attrs={
				'class':'form-control',
				'placeholder':'votre nom Utilisateur'

				}
			))

	password = forms.CharField(
		label='Mot de passe',
		widget=forms.PasswordInput(
			attrs={
				'class':'form-control',
				'type':'password',
				'placeholder':'votre mot de passe'


				}
			))

	password1 = forms.CharField(
		label = 'Password1',
		widget = forms.PasswordInput(
			attrs ={ 
				'placeholder':'password1',
				'type':'password',
				'class':'form-control'
				}
			)

		)
	nom = forms.CharField(
		label = 'Nom',
		widget = forms.TextInput(
			attrs ={ 
				'placeholder':'Votre nom',
				'class':'form-control'
				}
			)

		)
	prenom = forms.CharField(
		label = 'Prenom',
		widget = forms.TextInput(
			attrs ={ 
				'placeholder':'Votre prenom',
				'class':'form-control'
				}
			)

		)

class AuteurForms(forms.ModelForm):

	username = forms.CharField(
		label='Nom Utilisateur',
		widget=forms.TextInput(
			attrs={
				'class':'form-control',
				'placeholder':'votre nom Utilisateur'

				}
			))

	password = forms.CharField(
		label='Mot de passe',
		widget=forms.PasswordInput(
			attrs={
				'class':'form-control',
				'type':'password',
				'placeholder':'votre mot de passe'


				}
			))

	password1 = forms.CharField(
		label = 'Password1',
		widget = forms.PasswordInput(
			attrs ={ 
				'placeholder':'password1',
				'type':'password',
				'class':'form-control'
				}
			)

		)
	nom = forms.CharField(
		label = 'Nom',
		widget = forms.TextInput(
			attrs ={ 
				'placeholder':'Votre nom',
				'class':'form-control'
				}
			)

		)
	prenom = forms.CharField(
		label = 'Prenom',
		widget = forms.TextInput(
			attrs ={ 
				'placeholder':'Votre prenom',
				'class':'form-control'
				}
			)

		)

	age = forms.IntegerField(
		label = 'Age',
		widget = forms.NumberInput(
			attrs ={ 
				'placeholder':'Votre Age',
				'class':'form-control'
				}
			)

		)

class LivreForms(forms.ModelForm):

	isbn = forms.IntegerField(
		label='',
		widget=forms.NumberInput(
			attrs={
				'class':'form-control',


				}
			))

	titre = forms.CharField(
		label='intitule',
		widget=forms.TextInput(
			attrs={
				'class':'form-control',
				'placeholder':'titre du livre'

				}
			))

	auteur = forms.ModelChoiceField(
		label='nom',
		queryset = Auteur.objects.all(),
		widget=forms.Select(
			attrs={
				'class':'form-control',

				}
			))

	emplacement = forms.ModelChoiceField(
		label='intitule',
		queryset = Emplacement.objects.all(),
		widget=forms.Select(
			attrs={
				'class':'form-control',

				}
			))

	annee_publication = forms.DateField(
		label='intitule',
		widget=forms.DateInput(
			attrs={
				'class':'form-control',

				}
			))

	nombre_exemplaire = forms.IntegerField(
		label='intitule',
		widget=forms.NumberInput(
			attrs={
				'class':'form-control',

				}
			))


	class Meta:
		model = Livre
		fields = '__all__'
		
class LecteurForms(forms.ModelForm):

	username = forms.CharField(
		label = 'Username',
		widget = forms.TextInput(
			attrs = {
				'placeholder':'username',
				'class':'form-control'


				}


			)
		)
	password = forms.CharField(
		label = 'Password',
		widget = forms.PasswordInput(
			attrs ={ 
				'placeholder':'password',
				'type':'password',
				'class':'form-control'
				}
			)

		)
	password1 = forms.CharField(
		label = 'Password1',
		widget = forms.PasswordInput(
			attrs ={ 
				'placeholder':'password1',
				'type':'password',
				'class':'form-control'
				}
			)

		)
	nom = forms.CharField(
		label = 'Nom',
		widget = forms.TextInput(
			attrs ={ 
				'placeholder':'Votre nom',
				'class':'form-control'
				}
			)

		)
	prenom = forms.CharField(
		label = 'Prenom',
		widget = forms.TextInput(
			attrs ={ 
				'placeholder':'Votre prenom',
				'class':'form-control'
				}
			)

		)
	age = forms.IntegerField(
		label = 'Age',
		widget = forms.NumberInput(
			attrs ={ 
				'placeholder':'Votre Age',
				'class':'form-control'
				}
			)

		)

class StatutForms(forms.ModelForm):

	class Meta:
		model = Statut
		fields = '__all__'

class ActionsForms(forms.ModelForm):

	bibliothecaire = forms.ModelChoiceField(
		label='',
		queryset = Bibliothecaire.objects.all(),
		widget=forms.Select(
			attrs={
				'class':'form-control',

				}
			))

	lecteur = forms.ModelChoiceField(
		label='',
		queryset = Lecteur.objects.all(),
		widget=forms.Select(
			attrs={
				'class':'form-control',

				}
			))


	livre = forms.ModelChoiceField(
		label='',
		queryset = Livre.objects.all(),
		widget=forms.Select(
			attrs={
				'class':'form-control',

				}
			))


	statut = forms.ModelChoiceField(
		label='',
		queryset = Statut.objects.all(),
		widget=forms.Select(
			attrs={
				'class':'form-control',

				}
			))

	class Meta:
		model = Actions
		fields = '__all__'

class Maison_EditionForms(forms.ModelForm):

		nom = forms.CharField(
		label = 'Nom',
		widget = forms.TextInput(
			attrs ={ 
				'placeholder':'Votre nom',
				'class':'form-control'
				}
			)

		)

		pays = forms.CharField(
		label = 'Pays',
		widget = forms.TextInput(
			attrs ={ 
				'placeholder':'Votre pays',
				'class':'form-control'
				}
			)

		)

		ville = forms.CharField(
		label = 'ville',
		widget = forms.TextInput(
			attrs ={ 
				'placeholder':'Votre ville',
				'class':'form-control'
				}
			)

		)

		quartier = forms.CharField(
		label = 'Quartier',
		widget = forms.TextInput(
			attrs ={ 
				'placeholder':'Votre quartier',
				'class':'form-control'
				}
			)

		)

		avenue = forms.CharField(
		label = 'Avenue',
		widget = forms.TextInput(
			attrs ={ 
				'placeholder':'Votre avenue',
				'class':'form-control'
				}
			)

		)

		auteur = forms.ModelChoiceField(
		label = 'Auteur',
		queryset = Auteur.objects.all(),
		widget = forms.Select(
			attrs ={ 
				'placeholder':'Votre nom',
				'class':'form-control'
				}
			)

		)

		livre = forms.ModelChoiceField(
		label = 'Livre',
		queryset = Livre.objects.all(),
		widget = forms.Select(
			attrs ={ 
				'placeholder':'Votre nom',
				'class':'form-control'
				}
			)

		)

		class Meta:
			model = Actions
			fields = '__all__'







