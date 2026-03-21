from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Alumno
from .forms import AlumnoForm


def alumno_list(request):
    query = request.GET.get('q', '')
    alumnos = Alumno.objects.all()

    if query:
        alumnos = alumnos.filter(nombre__icontains=query) | \
                  alumnos.filter(apellido__icontains=query) | \
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


# 🔹 VISTAS EXTRA
def cursos_list(request):
    return render(request, "alumno/cursos.html")


def catedraticos_list(request):
    return render(request, "alumno/catedraticos.html")


def asignaciones_list(request):
    return render(request, "alumno/asignaciones.html")


def inscripciones_list(request):
    return render(request, "alumno/inscripciones.html")


def notas_list(request):
    return render(request, "alumno/notas.html")