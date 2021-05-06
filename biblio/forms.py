from django import forms
from .models import *
class BibliothecaireForms(forms.Form):

	username = forms.CharField(
		label='Nom Utilisateur',
		widget=forms.TextInput(
			attrs={
				'class':'form-control',
				'placeholder':'votre nom Utilisateur',
				'required.':'False',

				}
			))

	password = forms.CharField(
		label='Mot de passe',
		widget=forms.PasswordInput(
			attrs={
				'class':'form-control',
				'type':'password',
				'placeholder':'votre mot de passe',


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
	matricule = forms.CharField(
		label = 'Matricule',
		widget = forms.TextInput(
			attrs ={ 
				'placeholder':'Votre Matricule',
				'class':'form-control'
				}
			)

		)

class AuteurForms(forms.Form):

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
	class Meta:
		model = Auteur
		fields = '__all__'

	

class EmplacementForms(forms.Form):

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

class LivreForms(forms.ModelForm):

	isbn = forms.IntegerField(
		label='NumeroLivre',
		widget=forms.NumberInput(
			attrs={
				'class':'form-control',


				}
			))

	titre = forms.CharField(
		label='Titre',
		widget=forms.TextInput(
			attrs={
				'class':'form-control',
				'placeholder':'titre du livre'

				}
			))

	auteur = forms.ModelChoiceField(
		label='Auteur',
		queryset = Auteur.objects.all(),
		widget=forms.Select(
			attrs={
				'class':'form-control',

				}
			))

	emplacement = forms.ModelChoiceField(
		label='Emplacement',
		queryset = Emplacement.objects.all(),
		widget=forms.Select(
			attrs={
				'class':'form-control',

				}
			))

	annee_publication = forms.DateField(
		label='AnneePublication',
		widget=forms.TextInput(
			attrs={
				'class':'form-control',
				'type':'date',

				}
			))

	nombre_exemplaire = forms.IntegerField(
		label='Exemplaire',
		widget=forms.NumberInput(
			attrs={
				'class':'form-control',

				}
			))


	class Meta:
		model = Livre
		fields = '__all__'
		
class LecteurForms(forms.Form):

	numero_carte = forms.IntegerField(
		label = 'Numero_Carte',
		widget = forms.NumberInput(
			attrs ={ 
				'placeholder':'numero_carte',
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

	fonction = forms.CharField(
		label = 'Fonction',
		widget = forms.TextInput(
			attrs ={ 
				'placeholder':'Votre fonction',
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
	class Meta:
		model = Lecteur
		fields = '__all__'

class ActionsForms(forms.Form):

	bibliothecaire = forms.ModelChoiceField(
		label='Bibliothecaire',
		queryset = Bibliothecaire.objects.all(),
		widget=forms.Select(
			attrs={
				'class':'form-control',

				}
			))

	lecteur = forms.ModelChoiceField(
		label='Lecteur',
		queryset = Lecteur.objects.all(),
		widget=forms.Select(
			attrs={
				'class':'form-control',

				}
			))


	livre = forms.ModelChoiceField(
		label='Livre',
		queryset = Livre.objects.all(),
		widget=forms.Select(
			attrs={
				'class':'form-control',

				}
			))

	statut = forms.TypedChoiceField(
		label = 'Statut',
		choices=((0, 'False'), (1, 'True')),
                   widget=forms.RadioSelect)

	class Meta:
		model = Actions
		fields = '__all__'

class ConnexionForm(forms.Form):
	username = forms.CharField(
		label = 'Username',
		widget=forms.TextInput(
			attrs={
				'placeholder':'username',
				'type':'username',
				'class':'form-control'
			}

		))

	password = forms.CharField(
		label = 'Password',
		widget = forms.PasswordInput(
			attrs ={ 
				'placeholder':'password',
				'type':'password',
				'class':'form-control'
				}
			))

class SearchForm(forms.Form):
	search = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'name':'q',
				'type':'search',
				'placeholder':'search by book name',
			}))





