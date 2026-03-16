from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Cours, Enseignant
from .forms import CoursForm, EnseignantForm

# Create your views here.

@login_required
def liste_cours(request):
    cours = Cours.objects.all()
    return render(request, 'cours/liste_cours.html', {'cours': cours})

def accueil(request):
    return render(request, 'cours/accueil.html')

@login_required
def ajouter_cours(request):
    form = CoursForm()
    if request.method == 'POST':
        form = CoursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_cours')
    return render(request, 'cours/ajouter_cours.html', {'form': form})

@login_required
def modifier_cours(request, id):
    cours = get_object_or_404(Cours, id=id)
    if request.method == 'POST':
        form = CoursForm(request.POST, instance=cours)
        if form.is_valid():
            form.save()
            return redirect('liste_cours')
    else:
        form = CoursForm(instance=cours)
    return render(request, 'cours/modifier_cours.html', {'form': form})

@login_required
def supprimer_cours(request, id):
    cours = get_object_or_404(Cours, id=id)
    cours.delete()
    return redirect('liste_cours')

def connexion_utilisateur(request):
    message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('liste_cours')
        else:
            message = "Nom d'utilisateur ou mot de passe incorrect."
    return render(request, 'cours/connexion.html', {'message': message})

def deconnexion_utilisateur(request):
    logout(request)
    return redirect('connexion')

# Vues pour les enseignants
@login_required
def liste_enseignants(request):
    enseignants = Enseignant.objects.all()
    return render(request, 'cours/liste_enseignants.html', {'enseignants': enseignants})

@login_required
def ajouter_enseignant(request):
    form = EnseignantForm()
    if request.method == 'POST':
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_enseignants')
    return render(request, 'cours/ajouter_enseignant.html', {'form': form})

@login_required
def modifier_enseignant(request, id):
    enseignant = get_object_or_404(Enseignant, id=id)
    if request.method == 'POST':
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return redirect('liste_enseignants')
    else:
        form = EnseignantForm(instance=enseignant)
    return render(request, 'cours/modifier_enseignant.html', {'form': form})

@login_required
def supprimer_enseignant(request, id):
    enseignant = get_object_or_404(Enseignant, id=id)
    enseignant.delete()
    return redirect('liste_enseignants')
