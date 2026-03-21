from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Alumno, Cursos, Catedratico
from .forms import AlumnoForm, CursoForm, CatedraticoForm

from .models import AsignacionCurso
from .forms import AsignacionCursoForm

from .models import InscripcionAlumno
from .forms import InscripcionAlumnoForm

from .models import Nota
from .forms import NotaForm


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



def inscripciones_list(request):
    inscripciones = InscripcionAlumno.objects.select_related('alumno', 'asignacion')
    form = InscripcionAlumnoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Inscripción realizada correctamente.')
            return redirect('alumno:inscripciones_list')
        else:
            messages.error(request, 'Error al inscribir.')

    return render(request, 'alumno/inscripciones.html', {
        'inscripciones': inscripciones,
        'form': form
    })


def inscripcion_edit(request, pk):
    inscripcion = get_object_or_404(InscripcionAlumno, pk=pk)
    form = InscripcionAlumnoForm(request.POST or None, instance=inscripcion)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Inscripción actualizada.')
            return redirect('alumno:inscripciones_list')

    return render(request, 'alumno/inscripcion_form.html', {
        'form': form,
        'title': 'Editar Inscripción'
    })


def inscripcion_delete(request, pk):
    inscripcion = get_object_or_404(InscripcionAlumno, pk=pk)

    if request.method == 'POST':
        inscripcion.delete()
        messages.success(request, 'Inscripción eliminada.')
        return redirect('alumno:inscripciones_list')

    return redirect('alumno:inscripciones_list')

def notas_list(request):
    return render(request, "alumno/notas.html")


def notas_list(request):
    notas = Nota.objects.select_related(
        'inscripcion__alumno',
        'inscripcion__asignacion__curso',
        'inscripcion__asignacion__catedratico'
    )

    form = NotaForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Nota registrada correctamente.')
            return redirect('alumno:notas_list')
        else:
            messages.error(request, 'Error al guardar la nota.')

    return render(request, 'alumno/notas.html', {
        'notas': notas,
        'form': form
    })


def nota_edit(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    form = NotaForm(request.POST or None, instance=nota)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Nota actualizada.')
            return redirect('alumno:notas_list')

    return render(request, 'alumno/nota_form.html', {
        'form': form,
        'title': 'Editar Nota'
    })


def nota_delete(request, pk):
    nota = get_object_or_404(Nota, pk=pk)

    if request.method == 'POST':
        nota.delete()
        messages.success(request, 'Nota eliminada.')
        return redirect('alumno:notas_list')

    return redirect('alumno:notas_list')