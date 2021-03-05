from django.db import models
from django.contrib.auth.models import User

class Bibliothecaire(models.Model):

	user = models.ForeignKey(User,on_delete = models.CASCADE)
	date_naissance = models.DateField()
	matricule = models.CharField(max_length=10)

class Auteur(models.Model):

	nom = models.CharField(max_length=20)
	prenom = models.CharField(max_length=20)

	def __str__(self):
		return f"Nom :{self.nom} Prenom :{self.prenom}"

class Emplacement(models.Model):

	etagere = models.CharField(max_length=10)
	numero = models.IntegerField()

	def __str__(self):
		return f" Etagere : {self.etagere} Numero : {self.numero}"

class Livre(models.Model):

	isbn = models.IntegerField()
	titre =models.CharField(max_length=20)  
	auteur = models.ForeignKey(Auteur, on_delete = models.CASCADE)
	emplacement = models.ForeignKey(Emplacement, on_delete=models.CASCADE)
	annee_publication = models.DateField()
	nombre_exemplaire = models.IntegerField()

	def __str__(self):
		return f" ISBN : {self.isbn} Title : {self.titre} Auteur : {self.auteur} Emplacement : {self.emplacemnt} Annee_Publication : {self.annee_publication} Nombre_Exemplaire{self.nombre_exemplaire}  "
		
class Lecteur(models.Model):
	
	numero_carte = models.CharField(max_length=20)
	nom = models.CharField(max_length=20)
	prenom = models.CharField(max_length=20)
	fonction = models.CharField(max_length=20)
	age = models.DateField()

	def __str__(self):
		return f" Numero_Carte : {self.numero_carte} Nom : {self.nom} Fonction : {self.fonction} Age : {self.age}"

class Actions(models.Model):

	bibliothecaire = models.ForeignKey(Bibliothecaire, on_delete=models.CASCADE)
	lecteur = models.ForeignKey(Lecteur, on_delete=models.CASCADE)  
	livre=models.ForeignKey(Livre,on_delete=models.CASCADE)
	statut=models.BooleanField(default=False)

	def __str__(self):
		return f" Bibliothecaire : {self.bibliothecaire} Lecteur : {self.lecteur} Statut : {self.statut}"
		















