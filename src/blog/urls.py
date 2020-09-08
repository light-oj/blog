from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from filebrowser.sites import site


from posts.views import index, blog, post, search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog, name='post-list'),
    path('search/', search, name='search'),
    path('post/<id>/', post, name='post-detail'),
    path('tinymce/', include('tinymce.urls')),
    path('admin/filebrowser/', site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )