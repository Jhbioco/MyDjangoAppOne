from django.contrib import admin
from .models import Paciente, Medico, Especialidade

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Especialidade)

