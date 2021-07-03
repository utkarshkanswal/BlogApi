from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from froala_editor import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls")),
    path('froala_editor/', include('froala_editor.urls')),
]
