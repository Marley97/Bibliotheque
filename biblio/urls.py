from django.contrib import admin
from django.urls import path
from .import views

urlpatterns=[	
	path('profile/', views.profil, name="profile"),
	path('emplacement/',views.Emplacement, name="emplacement")
	
]

