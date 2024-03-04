from django.db import models
from django.core.exceptions import ValidationError

class SingletonModel(models.Model):
    class Meta:
        abstract = True

class Image(SingletonModel):
    title = models.CharField(max_length=255, default='deslindes')
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = 'deslindes'  # Asegurarse de que el título siempre sea 'deslindes'
        if Image.objects.exclude(pk=self.pk).exists():
            # Si ya existe otro registro, no permitir un nuevo registro
            raise ValidationError('Ya existe un registro. No se puede crear otro.')
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            # Si no existe, se puede crear uno nuevo y retornarlo
            # O simplemente retornar None o lanzar un error según la lógica deseada
            return None

    class Meta:
        verbose_name = "Imagen Deslindes"
        verbose_name_plural = "Imagen Deslindes"