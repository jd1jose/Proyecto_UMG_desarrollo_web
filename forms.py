from django import forms
from .models import Usuario, Vacante, Candidato, InformeRiesgo
from django.contrib.auth import get_user_model
User = get_user_model()
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'rol', 'is_active']

class VacanteForm(forms.ModelForm):
    class Meta:
        model = Vacante
        fields = ['usuario', 'empresa', 'puesto', 'area', 'requisitos', 'estado']
        widgets = {
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la Empresa'}),
            'puesto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el puesto'}),
            'area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Área de la vacante'}),
            'requisitos': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Escriba los requisitos de la vacante...'
            }),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = '__all__'

class InformeRiesgoForm(forms.ModelForm):
    class Meta:
        model = InformeRiesgo
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=False,
        label="Contraseña"
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=False,
        label="Confirmar Contraseña"
    )
    class Meta:
        model = User
        fields = ["username", "email", "rol", "is_active", "password", "confirm_password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "rol": forms.Select(attrs={"class": "form-control"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password or confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Las contraseñas no coinciden")

            return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        if password:
            user.set_password(password)  # 🔒 encriptar contraseña
        if commit:
            user.save()
        return user