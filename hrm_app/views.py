from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Usuario, Vacante, Candidato, InformeRiesgo
from .forms import UsuarioForm, VacanteForm, CandidatoForm, InformeRiesgoForm
from django.contrib.auth import get_user_model
from functools import wraps
User = get_user_model()

def role_required(roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            if request.user.rol not in roles:
                return redirect('dashboard')  
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.rol == "candidato":
                return redirect('candidato_create')
            elif user.rol == "reclutador":
                return redirect('vacantes')
            elif user.rol == "administrador":
                return redirect('dashboard')
            else:
                return redirect('dashboard')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
    return render(request, 'hrm_app/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'hrm_app/dashboard.html')

# ----- CRUD VACANTES -----
@login_required
@role_required(['reclutador','administrador'])
def vacantes_list(request):
    vacantes = Vacante.objects.all()
    return render(request, 'hrm_app/vacantes.html', {'vacantes': vacantes})

@login_required
@role_required(['reclutador','administrador'])
def vacante_create(request):
    if request.method == 'POST':
        form = VacanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacantes')
    else:
        form = VacanteForm()
    return render(request, 'hrm_app/form.html', {'form': form, 'titulo': 'Nueva Vacante'})

@login_required
@role_required(['reclutador','administrador'])
def vacante_edit(request, pk):
    vacante = get_object_or_404(Vacante, pk=pk)
    if request.method == 'POST':
        form = VacanteForm(request.POST, instance=vacante)
        if form.is_valid():
            form.save()
            return redirect('vacantes')
    else:
        form = VacanteForm(instance=vacante)
    return render(request, 'hrm_app/form.html', {'form': form, 'titulo': 'Editar Vacante'})

@login_required
@role_required(['reclutador','administrador'])
def vacante_delete(request, pk):
    vacante = get_object_or_404(Vacante, pk=pk)
    vacante.delete()
    return redirect('vacantes')

# ----- CRUD CANDIDATOS -----
@login_required
@role_required(['candidato','reclutador','administrador'])
def candidatos_list(request):
    candidatos = Candidato.objects.all()
    return render(request, 'hrm_app/candidatos.html', {'candidatos': candidatos})

@login_required
@role_required(['candidato','reclutador','administrador'])
def candidato_create(request):
    if request.method == 'POST':
        form = CandidatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('candidatos')
    else:
        form = CandidatoForm()
    return render(request, 'hrm_app/form.html', {'form': form, 'titulo': 'Nuevo Candidato'})

@login_required
@role_required(['candidato','reclutador','administrador'])
def candidato_edit(request, pk):
    candidato = get_object_or_404(Candidato, pk=pk)
    if request.method == 'POST':
        form = CandidatoForm(request.POST, request.FILES, instance=candidato)
        if form.is_valid():
            form.save()
            return redirect('candidatos')
    else:
        form = CandidatoForm(instance=candidato)
    return render(request, 'hrm_app/form.html', {'form': form, 'titulo': 'Editar Candidato'})

@login_required
@role_required(['candidato','reclutador','administrador'])
def candidato_delete(request, pk):
    candidato = get_object_or_404(Candidato, pk=pk)
    candidato.delete()
    return redirect('candidatos')

# ----- CRUD INFORME DE RIESGO -----
@login_required
@role_required(['reclutador','administrador'])
def informes_list(request):
    informes = InformeRiesgo.objects.all()
    return render(request, 'hrm_app/informe_riesgo.html', {'informes': informes})

@login_required
@role_required(['reclutador','administrador'])
def informe_create(request):
    if request.method == 'POST':
        form = InformeRiesgoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('informe_riesgo')
    else:
        form = InformeRiesgoForm()
    return render(request, 'hrm_app/form.html', {'form': form, 'titulo': 'Nuevo Informe de Riesgo'})

@login_required
@role_required(['administrador'])
def usuarios_list(request):
    usuarios = User.objects.all()
    return render(request, 'hrm_app/usuarios.html', {'usuarios': usuarios})

@login_required
@role_required(['administrador'])
def usuario_create(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuarios")
    else:
        form = UsuarioForm()
    return render(request, "hrm_app/usuario_form.html", {"form": form, "accion": "Crear"})

# Editar usuario
@login_required
@role_required(['administrador'])
def usuario_edit(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect("usuarios")
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, "hrm_app/usuario_form.html", {"form": form, "accion": "Editar"})

# Desactivar / Activar usuario
@login_required
def usuario_toggle(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    usuario.is_active = not usuario.is_active
    usuario.save()
    return redirect("usuarios")