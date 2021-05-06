from django.contrib import admin
from django.urls import path
from .import views

urlpatterns=[	
	path('profile/', views.profil_view, name="profile"),
	path('emplacement/',views.emplacement, name="emplacement"),
	path('auteur/',views.auteur, name="auteur"),
	path('livre/',views.livre, name="livre"),
	path('lecteur/',views.lecteur, name="lecteur"),
	path('liste/',views.listes, name="listeL"),
	path('modifier/<int:id>/',views.modifier_livre, name="updateL"),
	path('delete/<int:id>/',views.delete_livre, name="deleteL"),
	path('registerB/',views.registerbibliothecaire,name='registerbibli'),
	path('listes/',views.listes,name='listesL'),
	path('action/',views.action,name='actionbibli'),
	path('livreemprunte/',views.livreemprunte,name='livreE'),
	path('livreremis/',views.livreremis,name='livreR'),
	path('result/<str:queryset>',views.result,name='result'),
 	path('connexion/',views.connexion,name='login'),
    path('deconnexion/',views.deconnexion,name='logout'),
	
]
