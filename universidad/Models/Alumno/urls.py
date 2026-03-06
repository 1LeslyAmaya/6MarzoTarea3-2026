from django.urls import path
from . import views


app_name = 'alumno'

urlpatterns = [
    path('',                     views.alumno_list,   name='list'),
    path('crear/',               views.alumno_create, name='create'),
    path('<int:pk>/',            views.alumno_detail, name='detail'),
    path('<int:pk>/editar/',     views.alumno_edit,   name='edit'),
    path('<int:pk>/eliminar/',   views.alumno_delete, name='delete'),

    path('cursos/',        views.cursos_list,        name='cursos_list'),
    path('catedraticos/',  views.catedraticos_list,  name='catedraticos_list'),
    path('asignaciones/',  views.asignaciones_list,  name='asignaciones_list'),
    path('inscripciones/', views.inscripciones_list, name='inscripciones_list'),
    path('notas/',         views.notas_list,         name='notas_list'),
]
