from django import forms

class RegistrationForm(forms.Form):
    GENDER = {
        '': 'Jenis Kelamin',
        'Laki-laki': 'Laki-Laki',
        'Perempuan': 'Perempuan'
    }

    RELIGION = {
        '': 'Agama',
        'Islam': 'Islam',
        'Kristen': 'Kristen',
        'Katolik': 'Katolik',
        'Hindu': 'Hindu',
        'Budha': 'Budha'
    }
    defaul_class = {'text-input' : 'form-control', 'select-input': 'form-select'}

    MARITAL_STATUS = {'Menikah': 'Menikah', 'Belum Menikah': 'Belum Menikah'}
    herb8_select = {0: 'Keluarga / Teman', 1: 'Brosur / Koran', 2: 'Spanduk / Baliho', 3: 'Facebook', 4: 'Instagram', 5: 'Lainnya'}

    full_name = forms.CharField(max_length=100, widget=forms.TextInput(
                attrs={
                    'class': defaul_class['text-input'],
                    'placeholder': 'Nama Lengkap'
                }))
    gender = forms.ChoiceField(choices=GENDER, widget=forms.Select(
                attrs={
                    'class': defaul_class['select-input'],
                    'aria-label': 'Jenis Kelamin'
                }))
    religion = forms.ChoiceField(choices=RELIGION, widget=forms.Select(
                attrs={
                    'class': defaul_class['select-input'],
                    'aria-label': 'Agama'
                }),required=False)
    marital_status = forms.ChoiceField(choices=MARITAL_STATUS, widget=forms.Select(
                attrs={
                    'class': defaul_class['select-input'],
                    'aria-label': 'Status Pernikahan'
                }))
    birth_date = forms.DateField(widget=forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': defaul_class['text-input']
                }),required=False)
    birth_place = forms.CharField(max_length=100, widget=forms.TextInput(
                attrs={
                    'class': defaul_class['text-input'],
                    'placeholder': 'Tempat Lahir'
                }),required=False)
    occupation = forms.CharField(max_length=100, widget=forms.TextInput(
            attrs={
                'class': defaul_class['text-input'],
                'placeholder': 'Pekerjaan'
            }),required=False)
    address = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': defaul_class['text-input'],
            'placeholder': 'Alamat',
            'style': 'height: 95px;',
        }
    ))
    phone_number = forms.CharField(max_length=20, widget=forms.TextInput(
                attrs={
                    'class': defaul_class['text-input'],
                    'placeholder': 'No. Tlp'
                }))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': defaul_class['text-input'],
            'placeholder': 'email'
        }
    ),required=False)
    diagnose = forms.CharField(widget=forms.TextInput(
                attrs={
                    'class': defaul_class['text-input'],
                    'placeholder': 'Diagnosa Dokter'
                }),required=False)
    had_surgery = forms.ChoiceField(choices=[(True, 'Ya'), (False, 'Tidak')], widget=forms.Select(
        attrs={
            'class': defaul_class['select-input'],
        }
    ),required=False)
    herb8_info = forms.ChoiceField(choices=herb8_select, widget=forms.Select(
        attrs={
            'class': defaul_class['select-input']
        }
    ),required=False)

