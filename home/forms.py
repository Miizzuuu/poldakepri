from django import forms

class Registrasi(forms.Form):
    Nama = forms.CharField(max_length=100)
    E-mail = forms.CharField(widget=forms.Textarea)