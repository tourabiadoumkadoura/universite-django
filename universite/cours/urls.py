from django.urls import path
from .views import accueil, liste_cours, ajouter_cours, modifier_cours, supprimer_cours, connexion_utilisateur, deconnexion_utilisateur, liste_enseignants, ajouter_enseignant, modifier_enseignant, supprimer_enseignant

urlpatterns = [
    path('', accueil, name='accueil'),
    path('cours/', liste_cours, name='liste_cours'),
    path('ajouter/', ajouter_cours, name='ajouter_cours'),
    path('modifier/<int:id>/', modifier_cours, name='modifier_cours'),
    path('supprimer/<int:id>/', supprimer_cours, name='supprimer_cours'),
    path('connexion/', connexion_utilisateur, name='connexion'),
    path('deconnexion/', deconnexion_utilisateur, name='deconnexion'),
    # URLs pour les enseignants
    path('enseignants/', liste_enseignants, name='liste_enseignants'),
    path('enseignants/ajouter/', ajouter_enseignant, name='ajouter_enseignant'),
    path('enseignants/modifier/<int:id>/', modifier_enseignant, name='modifier_enseignant'),
    path('enseignants/supprimer/<int:id>/', supprimer_enseignant, name='supprimer_enseignant'),
]
