from django.contrib import admin
from django.utils.html import format_html
from .models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ('sitio', 'pic_tag', 'descripcion',  'etapa')
    list_editable = ('descripcion', 'etapa')

    def pic_tag(self, obj):
        return format_html('<img src="{}" style="max-height: 100px;">'.format(obj.pic.url))

    pic_tag.short_description = 'Imagen'

admin.site.register(Image, ImageAdmin)

