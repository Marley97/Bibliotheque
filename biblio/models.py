from django.db import models
from django.contrib.auth.models import User

class Emplacement(models.Model):

	etagere = models.CharField(max_length=10)
	numero = models.IntegerField()

	def __str__(self):
		return f" Etagere : {self.etegere} Numero : {self.numero}"

class Bibliothecaire(models.Model):

	user = models.ForeignKey(User,on_delete = models.CASCADE)
	nom = models.CharField(max_length=20)
	prenom = models.CharField(max_length=10)

class Auteur(models.Model):

	user = models.ForeignKey(User,on_delete = models.CASCADE)
	nom = models.CharField(max_length=20)
	prenom = models.CharField(max_length=20)
	age = models.DateField()

class Livre(models.Model):

	isbn= models.IntegerField()
	titre=models.CharField(max_length=20)  
	auteur = models.ForeignKey(Auteur, on_delete = models.CASCADE)
	emplacement = models.ForeignKey(Emplacement, on_delete=models.CASCADE)
	annee_publication = models.DateField()
	nombre_exemplaire = models.IntegerField()

	def __str__(self):
		return f" ISBN : {self.isbn} Title : {self.titre} Auteur : {self.auteur} Emplacement : {self.emplacemnt} Annee_Publication : {self.annee_publication} Nombre_Exemplaire{self.nombre_exemplaire}  "
		
class Lecteur(models.Model):

	user = models.ForeignKey(User,on_delete = models.CASCADE)
	nom = models.CharField(max_length=20)
	prenom = models.CharField(max_length=20)
	age = models.DateField()

class Statut(models.Model):

	statut = models.CharField(max_length=20)

class Actions(models.Model):

	bibliothecaire = models.ForeignKey(Bibliothecaire, on_delete=models.CASCADE)
	lecteur = models.ForeignKey(Lecteur, on_delete=models.CASCADE)  
	livre=models.ForeignKey(Livre,on_delete=models.CASCADE)
	statut=models.ForeignKey(Statut, on_delete=models.CASCADE)

	def __str__(self):
		return f" Bibliothecaire : {self.bibliothecaire} Lecteur : {self.lecteur} Statut : {self.statut}"
		
class Maison_Edition(models.Model):

	nom = models.CharField(max_length=20)
	pays = models.CharField(max_length=10)
	ville = models.CharField(max_length=10)
	quartier = models.CharField(max_length=15)
	avenue = models.CharField(max_length=10)
	auteur = models.ForeignKey(Auteur,on_delete=models.CASCADE)
	livre = models.ForeignKey(Livre,on_delete=models.CASCADE)

	def __str__(self):
		return f" Nom : {self.nom} Pays : {self.pays} Ville : {self.ville} Quartier : {self.quartier} Avenue : {self.avenue} Auteur : {self.auteur} Livre : {self.livre}"
















