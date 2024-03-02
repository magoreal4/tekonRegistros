from django.contrib import admin
from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Si ya existe al menos un registro, deshabilita la opción de añadir más.
        if Image.objects.exists():
            return False
        return super().has_add_permission(request)
