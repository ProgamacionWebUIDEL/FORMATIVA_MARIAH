from django.contrib import admin

# Register your models here.
from.models import Mascotas
from.models import Alimentos
from.models import Accesorios
admin.site.register(Mascotas)
admin.site.register(Alimentos)
admin.site.register(Accesorios)