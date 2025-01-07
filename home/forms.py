from django import forms


class Peserta(forms.Form):
    CHOICES = {
        "gender": [("laki laki", "Laki Laki"), ("perempuan", "Perempuan")],
        "country": [
            ("indonesia", "Indonesia"),
            ("malaysia", "Malaysia"),
            ("singapura", "Singapura"),
            ("lainya", "Lainya"),
        ],
        "blood": [
            ("a", "A"),
            ("b", "B"),
            ("ab", "AB"),
            ("o", "O"),
            ("tidak diketahui", "Tidak Diketahui"),
        ],
        "id_type": [
            ("ktp", "KTP"),
            ("sim", "SIM"),
            ("kartu pelajar", "Kartu Pelajar"),
            ("passport", "Passport"),
        ],
        "category": [
            ("umum", "Umum (dibawah 45 tahun)"),
            ("master", "Master (diatas 45 tahun)"),
        ],
        "yes_no": [("1", "Ya"), ("2", "Tidak")],
        "size": [("s", "S"), ("m", "M"), ("l", "L"), ("xl", "XL"), ("xxl", "XXL")],
    }

    HEALTH_QUESTIONS = [
        "Memiliki Riwayat Penyakit Jantung",
        "Memiliki Riwayat Penyakit Hipertensi",
        "Memiliki Riwayat Penyakit Kronik/Tahunan Lainnya (Diabetes Melitus, Ginjal, Hepatitis, dll)",
        "Memiliki Riwayat Penyakit Epilepsi dan/atau Gangguan Saraf Lainnya",
        "Memiliki Riwayat Penyakit Asma/Saluran Pernafasan Lainnya",
        "Memiliki Asuransi BPJS dan/atau Asuransi Lainnya",
        "Memiliki Riwayat Alergi Terhadap Obat Tertentu",
    ]

    nama = forms.CharField(max_length=50, label="Nama")
    email = forms.EmailField(max_length=80, label="E-Mail")
    jenis_kelamin = forms.ChoiceField(label="Jenis Kelamin", choices=CHOICES["gender"])
    tempat_lahir = forms.CharField(max_length=50, label="Tempat Lahir")
    birthday = forms.DateField(
        label="Birth Day", widget=forms.DateInput(attrs={"type": "date"})
    )
    phone = forms.CharField(max_length=12, label="Nomor Handphone")

    alamat = forms.CharField(max_length=80, label="Alamat")
    kota = forms.CharField(max_length=80, label="Kota")
    provinsi = forms.CharField(max_length=80, label="Provinsi")
    warga_negara = forms.ChoiceField(label="Warga Negara", choices=CHOICES["country"])

    gol_darah = forms.ChoiceField(label="Golongan Darah", choices=CHOICES["blood"])
    jenis_id = forms.ChoiceField(label="Jenis ID", choices=CHOICES["id_type"])
    no_id = forms.CharField(max_length=80, label="Nomor ID")
    f_id = forms.FileField(label="Upload KTP/ID Anda")
    kategori = forms.ChoiceField(label="Kategori", choices=CHOICES["category"])

    kontak_darurat = forms.CharField(max_length=80, label="Nama Kontak Darurat")
    no_kontak_darurat = forms.CharField(
        max_length=80, label="Nomor Telepon Kontak Darurat"
    )

    riwayat_penyakit_jantung = forms.ChoiceField(
        widget=forms.RadioSelect, choices=CHOICES["yes_no"], label=HEALTH_QUESTIONS[0]
    )
    riwayat_penyakit_hipertensi = forms.ChoiceField(
        widget=forms.RadioSelect, choices=CHOICES["yes_no"], label=HEALTH_QUESTIONS[1]
    )
    riwayat_penyakit_kronik = forms.ChoiceField(
        widget=forms.RadioSelect, choices=CHOICES["yes_no"], label=HEALTH_QUESTIONS[2]
    )
    riwayat_penyakit_epilepsi = forms.ChoiceField(
        widget=forms.RadioSelect, choices=CHOICES["yes_no"], label=HEALTH_QUESTIONS[3]
    )
    riwayat_penyakit_asma = forms.ChoiceField(
        widget=forms.RadioSelect, choices=CHOICES["yes_no"], label=HEALTH_QUESTIONS[4]
    )
    memiliki_asuransi = forms.ChoiceField(
        widget=forms.RadioSelect, choices=CHOICES["yes_no"], label=HEALTH_QUESTIONS[5]
    )
    riwayat_alergi_obat = forms.ChoiceField(
        widget=forms.RadioSelect, choices=CHOICES["yes_no"], label=HEALTH_QUESTIONS[6]
    )

    alergi = forms.CharField(
        max_length=80, label="Jika Iya Sebutkan Alergi", required=False
    )
    bib = forms.CharField(max_length=80, label="Nama Pada BIB")
    size_baju = forms.ChoiceField(label="Ukuran Baju", choices=CHOICES["size"])
    f_pembayaran = forms.FileField(label="Struk/Nota Konfirmasi Pembayaran")
