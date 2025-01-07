from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import Peserta as PesertaForm
from .models import Peserta


def home(request):
    if request.method == "POST":
        form = PesertaForm(request.POST, request.FILES)
        if form.is_valid():
            # Create Peserta instance from form data
            peserta = Peserta(
                nama=form.cleaned_data["nama"],
                email=form.cleaned_data["email"],
                jenis_kelamin=form.cleaned_data["jenis_kelamin"],
                tempat_lahir=form.cleaned_data["tempat_lahir"],
                birthday=form.cleaned_data["birthday"],
                phone=form.cleaned_data["phone"],
                alamat=form.cleaned_data["alamat"],
                kota=form.cleaned_data["kota"],
                provinsi=form.cleaned_data["provinsi"],
                warga_negara=form.cleaned_data["warga_negara"],
                gol_darah=form.cleaned_data["gol_darah"],
                jenis_id=form.cleaned_data["jenis_id"],
                no_id=form.cleaned_data["no_id"],
                f_id=form.cleaned_data["f_id"],
                kategori=form.cleaned_data["kategori"],
                kontak_darurat=form.cleaned_data["kontak_darurat"],
                no_kontak_darurat=form.cleaned_data["no_kontak_darurat"],
                riwayat_penyakit_jantung=form.cleaned_data["riwayat_penyakit_jantung"],
                riwayat_penyakit_hipertensi=form.cleaned_data[
                    "riwayat_penyakit_hipertensi"
                ],
                riwayat_penyakit_kronik=form.cleaned_data["riwayat_penyakit_kronik"],
                riwayat_penyakit_epilepsi=form.cleaned_data[
                    "riwayat_penyakit_epilepsi"
                ],
                riwayat_penyakit_asma=form.cleaned_data["riwayat_penyakit_asma"],
                memiliki_asuransi=form.cleaned_data["memiliki_asuransi"],
                riwayat_alergi_obat=form.cleaned_data["riwayat_alergi_obat"],
                alergi=form.cleaned_data["alergi"],
                bib=form.cleaned_data["bib"],
                size_baju=form.cleaned_data["size_baju"],
                f_pembayaran=form.cleaned_data["f_pembayaran"],
            )
            peserta.save()
            messages.success(request, "Pendaftaran berhasil!")
            return redirect("home")
        else:
            messages.error(request, "Mohon periksa kembali form anda.")
    else:
        form = PesertaForm()

    return render(request, "home.html", {"form": form})
