from django.shortcuts import render

from django.shortcuts import render
from universidad.Models.Alumno.models import Alumno
def dashboard(request):
    context = {
        'total_alumnos'   : Alumno.objects.count(),
        'activos'         : Alumno.objects.filter(is_active=True).count(),
        'inactivos'       : Alumno.objects.filter(is_active=False).count(),
    }
    return render(request, 'core/dashboard.html', context)


from django.shortcuts import render
from django.db.models import Avg
from universidad.Models.Alumno.models import InscripcionAlumno, Nota


def reporte_alumnos_cursos(request):

    datos = InscripcionAlumno.objects.select_related(
        'alumno',
        'asignacion__curso',
        'asignacion__catedratico'
    )

    return render(request, 'reportes/alumnos_cursos.html', {'datos': datos})


def reporte_promedio_cursos(request):

    datos = Nota.objects.values(
        'inscripcion__asignacion__curso__nombre'
    ).annotate(
        promedio=Avg('calificacion')
    )

    return render(request, 'reportes/promedio_cursos.html', {'datos': datos})


