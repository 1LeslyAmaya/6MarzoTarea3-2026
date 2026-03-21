from django import forms
from .models import Alumno, Cursos , Catedratico,  AsignacionCurso, InscripcionAlumno , Nota

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'gender',
            'birth_date',
            'is_active',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono (opcional)'
            }),
            'gender': forms.Select(
                choices=[('', '-- Seleccionar --'), ('M', 'Masculino'), ('F', 'Femenino')],
                attrs={'class': 'form-select'}
            ),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = '__all__'


class CatedraticoForm(forms.ModelForm):
    class Meta:
        model = Catedratico
        fields = ['first_name', 'last_name', 'email', 'phone', 'is_active']


class AsignacionCursoForm(forms.ModelForm):
    class Meta:
        model = AsignacionCurso
        fields = ['curso', 'catedratico', 'horario', 'aula', 'is_active']
        labels = {
            'curso': 'Curso',
            'catedratico': 'Catedrático',
            'horario': 'Horario',
            'aula': 'Aula',
            'is_active': 'Activo'
        }


class InscripcionAlumnoForm(forms.ModelForm):
    class Meta:
        model = InscripcionAlumno
        fields = ['alumno', 'asignacion']
        labels = {
            'alumno': 'Alumno',
            'asignacion': 'Asignación (Curso - Catedrático)'

        }


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['inscripcion', 'calificacion', 'observacion']
        labels = {
            'inscripcion': 'Inscripción',
            'calificacion': 'Calificación',
            'observacion': 'Observación'
        }