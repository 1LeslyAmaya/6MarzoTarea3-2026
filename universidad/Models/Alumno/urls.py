from django.urls import path
from . import views

app_name = 'alumno'

urlpatterns = [
    path('', views.alumno_list, name='list'),
    path('<int:pk>/editar/', views.alumno_edit, name='edit'),
    path('<int:pk>/eliminar/', views.alumno_delete, name='delete'),


    path('cursos/', views.cursos_list, name='cursos_list'),
    path('cursos/', views.cursos_list, name='cursos_list'),
    path('cursos/<int:pk>/editar/', views.curso_edit, name='curso_edit'),
    path('cursos/<int:pk>/eliminar/', views.curso_delete, name='curso_delete'),


    path('catedraticos/', views.catedraticos_list, name='catedraticos_list'),
    path('catedraticos/<int:pk>/editar/', views.catedratico_edit, name='catedratico_edit'),
    path('catedraticos/<int:pk>/eliminar/', views.catedratico_delete, name='catedratico_delete'),


    path('asignaciones/', views.asignaciones_list, name='asignaciones_list'),
    path('asignaciones/<int:pk>/editar/', views.asignacion_edit, name='asignacion_edit'),
    path('asignaciones/<int:pk>/eliminar/', views.asignacion_delete, name='asignacion_delete'),

    path('inscripciones/', views.inscripciones_list, name='inscripciones_list'),
    path('inscripciones/<int:pk>/editar/', views.inscripcion_edit, name='inscripcion_edit'),
    path('inscripciones/<int:pk>/eliminar/', views.inscripcion_delete, name='inscripcion_delete'),

    path('notas/', views.notas_list, name='notas_list'),
]