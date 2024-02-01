from django.http import HttpResponse
from django.shortcuts import render

from .forms import RegistrationForm
from .models import Registration

def index(request):
    # return HttpResponse("Hello, saya farid software engineer andalan anda")
    return render(request, 'medicio/index.html')

def registration(request):
    if request.method == 'POST':
        # print("iya ini")
        form = RegistrationForm(request.POST)
        print("raw data -> ", form.data)
        print("bbb")
        if form.is_valid():
            existing_record = Registration.objects.filter(
                # full_name=form.cleaned_data['full_name'],
                phone_number=form.cleaned_data['phone_number']
            ).exists()
            if not existing_record:
                form.save()
                form = RegistrationForm()
                HttpResponse("thank you")
            else:
                form.add_error(None, 'A record with the same name and phone number already exists.')
        else:
            print("form not valid")
            print(form.errors)
    else:
        print("ini yang pertama")
        form = RegistrationForm()
    return render(request, 'medicio/inner-page.html', {'form': form})

