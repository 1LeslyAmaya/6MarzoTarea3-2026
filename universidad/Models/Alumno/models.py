from django.db import models

class Alumno(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=1)
    birth_date = models.DateField()
    enrolled_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'alumno'


class Catedratico(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'catedratico'


class Curso(models.Model):
    nombre = models.CharField(max_length=120)
    codigo = models.CharField(max_length=20, unique=True)
    creditos = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    class Meta:
        db_table = 'curso'


class AsignacionCurso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    catedratico = models.ForeignKey(Catedratico, on_delete=models.PROTECT)
    horario = models.CharField(max_length=100)  # Ej: "Lun-Mie 18:00-20:00"
    aula = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.curso.codigo} / {self.catedratico} / {self.horario}"

    class Meta:
        db_table = 'asignacion_curso'


class InscripcionAlumno(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT)
    asignacion = models.ForeignKey(AsignacionCurso, on_delete=models.PROTECT)
    fecha_asignacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.alumno} -> {self.asignacion}"

    class Meta:
        db_table = 'inscripcion_alumno'


class Nota(models.Model):
    inscripcion = models.ForeignKey(InscripcionAlumno, on_delete=models.CASCADE)
    calificacion = models.DecimalField(max_digits=5, decimal_places=2)  # 0.00 a 100.00
    fecha_registro = models.DateTimeField(auto_now_add=True)
    observacion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.inscripcion} = {self.calificacion}"

    class Meta:
        db_table = 'nota'