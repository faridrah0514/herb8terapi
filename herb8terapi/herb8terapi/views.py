from django.http import HttpResponse
from django.shortcuts import render, redirect
import secrets

from .forms import RegistrationForm
from .models import Registration

def format_whatsapp_url(**values):
    wa_number = '6281299266009'
    formatted_text = f"""
Halo herb8.
Nama: {values['full_name']},
Jenis Kelamin: {values['gender']},
Status Perkawinan: {values['marital_status']},
Tempat/Tanggal Lahir: {values['birth_place']}, {values['birth_date'].strftime("%d-%m-%Y")},
Agama: {values['religion']},
Pekerjaan: {values['occupation']},
Alamat: {values['address']},
No. Tlp: {values['phone_number']},
Email: {values['email']},
Diagnosa dokter: {values['diagnose']},
Pernah Operasi: {'Ya' if values['had_surgery'] else 'Tidak'},
Tau Herb8 dari: {values['herb8_info']},
Link: https://herb8terapi.com/{values['rand_id']}
"""

    # Encode the formatted text for a URL
    encoded_text = formatted_text.replace(" ", "%20").replace("\n", "%0A")

    # Construct the WhatsApp URL
    whatsapp_url = f"https://api.whatsapp.com/send/?phone={wa_number}&text={encoded_text}"

    return whatsapp_url   

def index(request):
    return render(request, 'medicio/index.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            existing_record = Registration.objects.filter(
                phone_number=form.cleaned_data['phone_number']
            ).exists()
            if not existing_record:
                form.cleaned_data['rand_id'] = secrets.token_hex(8)
                Registration(**form.cleaned_data).save()
                return redirect(format_whatsapp_url(**form.cleaned_data))
            else:
                form.add_error(None, 'A record with the same name and phone number already exists.')  
    else:
        form = RegistrationForm()
    return render(request, 'medicio/inner-page.html', {'form': form})

def patient_info(request, rand_id):
    record = Registration.objects.get(
        rand_id=rand_id
    )
    if not record:
        return HttpResponse("NO RECORD")
    else:
        return render(request, 'medicio/base/patient_info.html', {'data': record})
