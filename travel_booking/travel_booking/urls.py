from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [path('admin/', admin.site.urls), path('', include('core.urls'))]
if settings.DEBUG:  # only for development
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])