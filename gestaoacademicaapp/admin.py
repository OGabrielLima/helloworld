from django.contrib import admin
# Register your models here.
from .models import Categoria, Conta, Despesa, Curso
admin.site.register(Categoria)
admin.site.register(Conta)
admin.site.register(Despesa)
admin.site.register(Curso)