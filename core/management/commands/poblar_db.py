from django.core.management.base import BaseCommand
from universidad.Models.Alumno.models import Alumno, Catedratico, Cursos, AsignacionCurso, InscripcionAlumno, Nota
import random
from datetime import date


class Command(BaseCommand):
    help = "Poblar la base de datos con 10000 registros por tabla"

    def handle(self, *args, **kwargs):

        alumnos = []
        catedraticos = []
        cursos = []
        asignaciones = []
        inscripciones = []

        # Crear alumnos
        for i in range(10000):
            alumno = Alumno.objects.create(
                first_name=f"Nombre{i}",
                last_name=f"Apellido{i}",
                email=f"alumno{i}@correo.com",
                phone=f"555{i}",
                gender=random.choice(["M", "F"]),
                birth_date=date(2000, 1, 1)
            )
            alumnos.append(alumno)

        self.stdout.write("Alumnos creados")

        # Crear catedráticos
        for i in range(10000):
            cat = Catedratico.objects.create(
                first_name=f"Catedratico{i}",
                last_name="Profesor",
                email=f"catedratico{i}@correo.com",
                phone=f"444{i}"
            )
            catedraticos.append(cat)

        self.stdout.write("Catedraticos creados")

        # Crear cursos
        for i in range(10000):
            curso = Cursos.objects.create(
                nombre=f"Curso {i}",
                codigo=f"C{i}",
                descripcion="Curso generado automaticamente",
                creditos=random.randint(3, 5)
            )
            cursos.append(curso)

        self.stdout.write("Cursos creados")

        # Crear asignaciones
        for i in range(10000):
            asignacion = AsignacionCurso.objects.create(
                curso=random.choice(cursos),
                catedratico=random.choice(catedraticos),
                horario="Lun-Mie 18:00-20:00",
                aula="A1"
            )
            asignaciones.append(asignacion)

        self.stdout.write("Asignaciones creadas")

        # Crear inscripciones
        for i in range(10000):
            ins = InscripcionAlumno.objects.create(
                alumno=random.choice(alumnos),
                asignacion=random.choice(asignaciones)
            )
            inscripciones.append(ins)

        self.stdout.write("Inscripciones creadas")

        # Crear notas
        for i in range(10000):
            Nota.objects.create(
                inscripcion=random.choice(inscripciones),
                calificacion=random.uniform(60, 100),
                observacion="Nota generada automáticamente"
            )

        self.stdout.write(self.style.SUCCESS("Base de datos poblada correctamente"))