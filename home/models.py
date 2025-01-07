from django.db import models


class Peserta(models.Model):
    GENDER_CHOICES = [("laki laki", "Laki Laki"), ("perempuan", "Perempuan")]
    COUNTRY_CHOICES = [
        ("indonesia", "Indonesia"),
        ("malaysia", "Malaysia"),
        ("singapura", "Singapura"),
        ("lainya", "Lainya"),
    ]
    BLOOD_CHOICES = [
        ("a", "A"),
        ("b", "B"),
        ("ab", "AB"),
        ("o", "O"),
        ("tidak diketahui", "Tidak Diketahui"),
    ]
    ID_CHOICES = [
        ("ktp", "KTP"),
        ("sim", "SIM"),
        ("kartu pelajar", "Kartu Pelajar"),
        ("passport", "Passport"),
    ]
    CATEGORY_CHOICES = [
        ("umum", "Umum (dibawah 45 tahun)"),
        ("master", "Master (diatas 45 tahun)"),
    ]
    SIZE_CHOICES = [("s", "S"), ("m", "M"), ("l", "L"), ("xl", "XL"), ("xxl", "XXL")]
    YES_NO_CHOICES = [(1, "Ya"), (2, "Tidak")]

    # informasi peserta
    id_peserta = models.CharField(max_length=4, unique=True, editable=False)
    nama = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    jenis_kelamin = models.CharField(max_length=10, choices=GENDER_CHOICES)
    tempat_lahir = models.CharField(max_length=50)
    birthday = models.DateField()
    phone = models.CharField(max_length=12)

    # alamat
    alamat = models.CharField(max_length=80)
    kota = models.CharField(max_length=80)
    provinsi = models.CharField(max_length=80)
    warga_negara = models.CharField(max_length=20, choices=COUNTRY_CHOICES)

    # identitas
    gol_darah = models.CharField(max_length=15, choices=BLOOD_CHOICES)
    jenis_id = models.CharField(max_length=15, choices=ID_CHOICES)
    no_id = models.CharField(max_length=80)
    f_id = models.FileField(upload_to="ids/")
    kategori = models.CharField(max_length=45, choices=CATEGORY_CHOICES)

    # kontak darurat
    kontak_darurat = models.CharField(max_length=80)
    no_kontak_darurat = models.CharField(max_length=80)

    # riwayat kesehatan
    riwayat_penyakit_jantung = models.IntegerField(choices=YES_NO_CHOICES)
    riwayat_penyakit_hipertensi = models.IntegerField(choices=YES_NO_CHOICES)
    riwayat_penyakit_kronik = models.IntegerField(choices=YES_NO_CHOICES)
    riwayat_penyakit_epilepsi = models.IntegerField(choices=YES_NO_CHOICES)
    riwayat_penyakit_asma = models.IntegerField(choices=YES_NO_CHOICES)
    memiliki_asuransi = models.IntegerField(choices=YES_NO_CHOICES)
    riwayat_alergi_obat = models.IntegerField(choices=YES_NO_CHOICES)

    # info tambahan
    alergi = models.CharField(max_length=80, blank=True)
    bib = models.CharField(max_length=80)
    size_baju = models.CharField(max_length=5, choices=SIZE_CHOICES)
    f_pembayaran = models.FileField(upload_to="payments/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama

    def save(self, *args, **kwargs):
        if not self.id_peserta:
            used_ids = set(Peserta.objects.values_list("id_peserta", flat=True))
            for i in range(1, 10000):
                candidate = str(i).zfill(4)
                if candidate not in used_ids:
                    self.id_peserta = candidate
                    break
        super().save(*args, **kwargs)
