from django.http import HttpResponse
from django.shortcuts import render, redirect
import secrets
import PyPDF2
from reportlab.pdfgen import canvas
from io import BytesIO
from django.conf import settings

from .forms import RegistrationForm
from .models import Registration

def format_whatsapp_url(**values):
    wa_number = '6281299266009'
    formatted_text = f"""
Halo herb8. Saya mau registrasi atas nama
Nama: {values['full_name']},
No. Tlp: {values['phone_number']},
Diagnosa dokter: {values['diagnose']},
Berikut detail dari registrasi saya
PDF Link: https://herb8terapi.com/pdf/{values['rand_id']}
"""
    old_formatted_text = f"""
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
PDF Link: https://herb8terapi.com/pdf/{values['rand_id']}
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
            # existing_record = Registration.objects.filter(
            #     phone_number=form.cleaned_data['phone_number']
            # ).exists()
            if True:
                form.cleaned_data['rand_id'] = secrets.token_hex(8)
                Registration(**form.cleaned_data).save()
                generate_pdf(form.cleaned_data['rand_id'])
                return redirect(format_whatsapp_url(**form.cleaned_data))
            else:
                form.add_error(None, 'A record with the same name and phone number already exists.')  
    else:
        form = RegistrationForm()
    return render(request, 'medicio/inner-page.html', {'form': form, 'title': 'Registrasi'})

def open_pdf(request, rand_id):
    # pdf_file = open(f'{settings.BASE_DIR}/static/pdf/dest/{rand_id}.pdf')
    # return HttpResponse("iya nih")
    with open(f'{settings.BASE_DIR}/static/pdf/dest/{rand_id}.pdf', 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{rand_id}.pdf"'
        return response

def generate_pdf(rand_id):
    # get patient record
    data = Registration.objects.get(
        rand_id=rand_id
    )
    religion_coordinate = {
        "Islam": 231,
        "Kristen": 281,
        "Katolik": 341,
        "Hindu": 396,
        "Buddha": 448,
        "Lainnya": 506
    }

    info_herb8_coordinate = {
        "Keluarga / Teman": (231, 277),
        "Facebook": (343, 277),
        "Instagram": (443, 277),
        "Brosur / Koran": (231, 259),
        "Spanduk / Baliho": (343, 259),
        "Lainnya": (443,259)
    }
    pdf_reader = PyPDF2.PdfReader(f'{settings.BASE_DIR}/static/pdf/src/docs.pdf')
    pdf_writer = PyPDF2.PdfWriter()
    page = pdf_reader.pages[0]
    packet = BytesIO()
    canvas_obj = canvas.Canvas(packet)
    canvas_obj.drawString(229, 648, f"{data.full_name}") # Nama Lengkap
    # Jenis Kelamin:
    if data.gender == "Perempuan":
        canvas_obj.drawString(349, 620, "V") 
    else:
        canvas_obj.drawString(232, 620, "V") # Laki-laki
    # Perempuan
    # Status Pernikahan:
        
    if data.marital_status == "Menikah":
        canvas_obj.drawString(232, 590, "V") # Menikah
    else:
        canvas_obj.drawString(349, 590, "V") # Belum Menikah
    # Tempat Tanggal Lahir
    canvas_obj.drawString(229, 562, f"{data.birth_place}, {data.birth_date}") 
    # Agama
    if data.religion:
        canvas_obj.drawString(religion_coordinate[data.religion], 535, "v") 

    canvas_obj.drawString(229, 506, f"{data.occupation}") # Pekerjaan
    canvas_obj.drawString(229, 478, f"{data.address}") # Alamat
    # canvas_obj.drawString(229, 449, "Larangan, Tangeran, Banten") # Alamat Line-2
    canvas_obj.drawString(229, 422, f"{data.phone_number}") # No Telepon
    canvas_obj.drawString(229, 393, f"{data.email}") # Email
    canvas_obj.drawString(229, 365, f"{data.diagnose}") #Diagnosa Dokter
   
    # Apakah Pernah Operasi?
    canvas_obj.drawString(232 if data.had_surgery else 293, 308, "V") # Ya
  
    # Info herb8
    if data.herb8_info:
         c = info_herb8_coordinate[data.herb8_info]
         canvas_obj.drawString(c[0], c[1], "v") 

    canvas_obj.save()
    packet.seek(0)
    overlay = PyPDF2.PdfReader(packet)
    page.merge_page(overlay.pages[0])
    pdf_writer.add_page(page)
    pdf_writer.write(f'{settings.BASE_DIR}/static/pdf/dest/{rand_id}.pdf')

def data_registration(request):
    data = Registration.objects.all()
    column_name = [field.name for field in Registration._meta.get_fields()]
    # print(data)
    print(column_name)
    column_name = ['Nama Lengkap', 'No. Tlp', 'Alamat', 'Gender', 'Agama', 'Status Pernikahan', 'Tempat/Tanggal Lahir', 'Pekerjaan',
                   'Email', 'Diagnosa', 'Pernah Operasi?', 'Info Herb8 Dari ?' 
                   ]
    return render(request, 'medicio/inner-page.html', {'data': data, 'column_name': column_name, 'title': 'Database'})
