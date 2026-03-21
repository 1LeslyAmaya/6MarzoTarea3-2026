from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Alumno, Cursos, Catedratico
from .forms import AlumnoForm, CursoForm, CatedraticoForm

from .models import AsignacionCurso
from .forms import AsignacionCursoForm

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

    if request.method == 'POST':
        curso.delete()
        messages.success(request, 'Curso eliminado.')
        return redirect('alumno:cursos_list')

    return redirect('alumno:cursos_list')


def catedraticos_list(request):
    query = request.GET.get('q', '')
    catedraticos = Catedratico.objects.all()

    if query:
        catedraticos = catedraticos.filter(first_name__icontains=query) | \
                       catedraticos.filter(last_name__icontains=query) | \
                       catedraticos.filter(email__icontains=query)

    form = CatedraticoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Catedrático registrado correctamente.')
            return redirect('alumno:catedraticos_list')
        else:
            messages.error(request, 'Error al guardar el catedrático.')

    return render(request, 'alumno/catedraticos.html', {
        'catedraticos': catedraticos,
        'query': query,
        'form': form
    })


def catedratico_edit(request, pk):
    catedratico = get_object_or_404(Catedratico, pk=pk)
    form = CatedraticoForm(request.POST or None, instance=catedratico)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Catedrático actualizado correctamente.')
            return redirect('alumno:catedraticos_list')
        else:
            messages.error(request, 'Error al actualizar.')

    return render(request, 'alumno/catedratico_form.html', {
        'form': form,
        'title': 'Editar Catedrático'
    })


def catedratico_delete(request, pk):
    catedratico = get_object_or_404(Catedratico, pk=pk)

    if request.method == 'POST':
        catedratico.delete()
        messages.success(request, 'Catedrático eliminado.')
        return redirect('alumno:catedraticos_list')

    return redirect('alumno:catedraticos_list')



def asignaciones_list(request):
    return render(request, "alumno/asignaciones.html")


def asignaciones_list(request):
    asignaciones = AsignacionCurso.objects.select_related('curso', 'catedratico')
    form = AsignacionCursoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Asignación creada correctamente.')
            return redirect('alumno:asignaciones_list')
        else:
            messages.error(request, 'Error al guardar.')

    return render(request, 'alumno/asignaciones.html', {
        'asignaciones': asignaciones,
        'form': form
    })


def asignacion_edit(request, pk):
    asignacion = get_object_or_404(AsignacionCurso, pk=pk)
    form = AsignacionCursoForm(request.POST or None, instance=asignacion)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Asignación actualizada.')
            return redirect('alumno:asignaciones_list')

    return render(request, 'alumno/asignacion_form.html', {
        'form': form,
        'title': 'Editar Asignación'
    })


def asignacion_delete(request, pk):
    asignacion = get_object_or_404(AsignacionCurso, pk=pk)

    if request.method == 'POST':
        asignacion.delete()
        messages.success(request, 'Asignación eliminada.')
        return redirect('alumno:asignaciones_list')

    return redirect('alumno:asignaciones_list')


def inscripciones_list(request):
    return render(request, "alumno/inscripciones.html")


def notas_list(request):
    return render(request, "alumno/notas.html")