from django.contrib import admin

from .models import Peserta


@admin.register(Peserta)
class PesertaAdmin(admin.ModelAdmin):
    list_display = ("id_peserta", "nama", "email", "kategori", "created_at")
    search_fields = ["id_peserta", "nama", "email", "no_id"]
    readonly_fields = ["id_peserta"]
    list_filter = ["kategori", "warga_negara"]
    ordering = ["id_peserta"]
