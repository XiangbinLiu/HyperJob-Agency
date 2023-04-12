from django.shortcuts import render
from django.views import generic
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import Vacancy
# Create your views here.


class VacanciesView(generic.ListView):
    template_name = 'vacancies.html'
    context_object_name = 'data'
    def get_queryset(self):
        return Vacancy.objects.all()

class MySignupView(generic.CreateView):
    form_class =  UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'

class DescriptionForm(forms.Form):
    description = forms.CharField(label="Description")

def main_page(request):
    return render(request, 'mainPage.html')

def home(request):
    if request.user.is_staff:
        form = DescriptionForm()
        return render(request, 'vacancy_new.html', {"form": form, "request":request})
    elif request.user.is_authenticated:
        form = DescriptionForm()
        return render(request, 'resume_new.html', {"form": form, "request":request})
    else:
        return render(request, 'mainPage.html')

def vacancy_create(request):
    if not request.user.is_staff:
        return render(request, 'vacancy_new.html', status=403)
    if request.method == 'POST':
        Vacancy.objects.create(description=request.POST["description"],
                               author=request.user)
        return render(request, 'mainPage.html')
    else:
        form = DescriptionForm()
        return render(request, 'vacancy_new.html', {"form": form, "request":request})


