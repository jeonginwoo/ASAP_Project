from django.contrib import admin
from .models import BurgerTable, SideTable, DDTable

admin.site.register(BurgerTable)
admin.site.register(SideTable)
admin.site.register(DDTable)