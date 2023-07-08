from django.contrib import admin
from .models import Rol,User,Category,Product,Boleta,Detalle_Boleta

# Register your models here.
admin.site.register(Rol)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Boleta)
admin.site.register(Detalle_Boleta)