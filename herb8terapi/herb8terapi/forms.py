from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Lengkap'}),
            'gender': forms.Select(attrs={'class': 'form-select', 'aria-label': 'Jenis Kelamin'}),
            'religion': forms.Select(attrs={'class': 'form-select', 'aria-label': 'Agama'}),
            'marital_status': forms.Select(attrs={'class': 'form-select', 'aria-label': 'Status Pernikahan'}),
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'birth_place': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tempat Lahir'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pekerjaan'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Alamat', 'style': 'height: 95px;'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'No. Tlp'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'diagnose': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Diagnosa Dokter'}),
            'had_surgery': forms.Select(attrs={'class': 'form-select'}),
            'herb8_info': forms.Select(attrs={'class': 'form-select'}),
        }