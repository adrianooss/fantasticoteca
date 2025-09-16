from django.contrib import admin
from .models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id','nome', 'legenda','publicada','categoria')
    list_display_links = ('id','nome', 'legenda')
    search_fields = ('nome',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    ordering = ('id',)
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)
