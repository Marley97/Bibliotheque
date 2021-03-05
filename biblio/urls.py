from django.contrib import admin
from django.urls import path
from .import views

urlpatterns=[	
	path('profile/', views.profil, name="profile"),
	path('emplacement/',views.emplacement, name="emplacement"),
	path('auteur/',views.auteur, name="auteur"),
	path('livre/',views.livre, name="livre"),
	path('lecteur/',views.lecteur, name="lecteur"),
	path('liste/',views.listes, name="listeL"),
	path('modifier/<int:id>/',views.modifier_livre, name="updateL"),
	path('delete/<int:id>/',views.delete_livre, name="deleteL")
	
]
