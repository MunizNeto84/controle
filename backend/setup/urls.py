
from django.contrib import admin
from django.urls import path
from controle.views import controles

urlpatterns = [
    path('admin/', admin.site.urls),
    path('controles/', controles),
]
