
from django.contrib import admin
from django.urls import path, include
from config import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('main.urls')),
    path("", include('formularios.urls')),
    path('', include('imagenes.urls')),
    # path("__reload__/", include("django_browser_reload.urls")),
]



if settings.DEBUG:

    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
