from django.http import HttpResponse
from django.shortcuts import render

from .forms import RegistrationForm

def index(request):
    # return HttpResponse("Hello, saya farid software engineer andalan anda")
    return render(request, 'medicio/index.html')

def registration(request):
    if request.method == 'POST':
        # print("iya ini")
        form = RegistrationForm(request.POST)
        print("bbb")
        if form.is_valid():
            # print("aaa")
            # print(dir(form))
            # print("full_name -> ", form.cleaned_data['full_name'])
            print("raw data -> ", form.data)
            print("cleaned_data -> ", form.cleaned_data)
            # print("lalalala")
            HttpResponse("thank you")
    else:
        print("ini yang pertama")
        form = RegistrationForm()
    return render(request, 'medicio/inner-page.html', {'form': form})

def registration_clone(request):
    if request.method == 'POST':
        # print("iya ini")
        form = RegistrationForm(request.POST)
        print("bbb")
        if form.is_valid():
            # print("aaa")
            # print(dir(form))
            # print("full_name -> ", form.cleaned_data['full_name'])
            print("raw data -> ", form.data)
            print("cleaned_data -> ", form.cleaned_data)
            # print("lalalala")
            HttpResponse("thank you")
    else:
        print("ini yang pertama")
        form = RegistrationForm()
    return render(request, 'medicio/base/registration_clone.html', {'form': form})

def registration_clone_2(request):
    if request.method == 'POST':
        # print("iya ini")
        form = RegistrationForm(request.POST)
        print("bbb")
        if form.is_valid():
            # print("aaa")
            # print(dir(form))
            # print("full_name -> ", form.cleaned_data['full_name'])
            print("raw data -> ", form.data)
            print("cleaned_data -> ", form.cleaned_data)
            # print("lalalala")
            HttpResponse("thank you")
    else:
        print("ini yang pertama")
        form = RegistrationForm()
    return render(request, 'medicio/base/registration_clone_2.html', {'form': form})

from django.shortcuts import render
from django.http import FileResponse
import imgkit
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def html_to_image(html, image_path):
    options = {
        'format': 'png',
        'width': 3507,  # Set the width to match A4 width
        'height': 2481,  # Set the height to match A4 height
    }
    print("di dalam")
    imgkit.from_string(html, '/User/farid.rahman/Personal')

def image_to_pdf(image_path, pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=A4)
    c.drawImage(image_path, 0, 0, width=3507, height=2481)
    c.showPage()
    c.save()

def download_pdf(request):
    # Replace 'your_template.html' with the actual template file containing user info
    print("sssss")
    html = render(request, 'medicio/base/registration_clone_2.html').content.decode('utf-8')
    
    # Replace 'output_image.png' with the desired image output path
    image_path = '/Users/farid.rahman/Personal/django/belajar-django-1/herb8terapi/herb8terapi/templates/medicio/base/'
    
    # Replace 'output_pdf.pdf' with the desired PDF output path
    pdf_path = '/Users/farid.rahman/Personal/django/belajar-django-1/herb8terapi/herb8terapi/templates/medicio/base/output_pdf.pdf'

    html_to_image(html, image_path)
    print("lllllll")
    image_to_pdf(image_path, pdf_path)

    with open(pdf_path, 'rb') as pdf_file:
        response = FileResponse(pdf_file, content_type='application/pdf')
        return response

