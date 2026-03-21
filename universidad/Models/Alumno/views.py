from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Alumno, Cursos
from .forms import AlumnoForm, CursoForm


# 🔹 ALUMNOS
def alumno_list(request):
    query = request.GET.get('q', '')
    alumnos = Alumno.objects.all()

    if query:
        alumnos = alumnos.filter(first_name__icontains=query) | \
                  alumnos.filter(last_name__icontains=query) | \
                  alumnos.filter(email__icontains=query)

    form = AlumnoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Alumno registrado correctamente.')
            return redirect('alumno:list')
        else:
            messages.error(request, 'Error al guardar el alumno.')

    return render(request, 'alumno/list.html', {
        'alumnos': alumnos,
        'query': query,
        'form': form
    })


def alumno_edit(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    form = AlumnoForm(request.POST or None, instance=alumno)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Alumno actualizado correctamente.')
            return redirect('alumno:list')
        else:
            messages.error(request, 'Error al actualizar.')

    return render(request, 'alumno/form.html', {
        'form': form,
        'title': 'Editar Alumno'
    })


def alumno_delete(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)

    if request.method == 'POST':
        alumno.delete()
        messages.success(request, 'Alumno eliminado.')
        return redirect('alumno:list')

    return redirect('alumno:list')


# 🔹 CURSOS (CRUD)
def cursos_list(request):
    cursos = Cursos.objects.all()
    form = CursoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso guardado correctamente.')
            return redirect('alumno:cursos_list')

    return render(request, 'alumno/cursos.html', {
        'cursos': cursos,
        'form': form
    })


def curso_edit(request, pk):
    curso = get_object_or_404(Cursos, pk=pk)
    form = CursoForm(request.POST or None, instance=curso)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso actualizado.')
            return redirect('alumno:cursos_list')

    return render(request, 'alumno/curso_form.html', {
        'form': form,
        'title': 'Editar Curso'
    })


def curso_delete(request, pk):
    curso = get_object_or_404(Cursos, pk=pk)
    curso.delete()
    messages.success(request, 'Curso eliminado.')
    return redirect('alumno:cursos_list')


# 🔹 OTRAS VISTAS
def catedraticos_list(request):
    return render(request, "alumno/catedraticos.html")


def asignaciones_list(request):
    return render(request, "alumno/asignaciones.html")


def inscripciones_list(request):
    return render(request, "alumno/inscripciones.html")


def notas_list(request):
    return render(request, "alumno/notas.html")