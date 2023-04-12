from django.views import generic
from django import forms
from django.shortcuts import render
from .models import Resume

# Create your views here.

class ResumesView(generic.ListView):
    template_name = 'resumes.html'
    context_object_name = 'data'
    def get_queryset(self):
        return Resume.objects.all()

class DescriptionForm(forms.Form):
    description = forms.CharField(label="Description")

def resume_create(request):
    if not request.user.is_authenticated:
        return render(request, 'resume_new.html', status=403)
    if request.method == 'POST':
        Resume.objects.create(description=request.POST["description"],
                               author=request.user)
        return render(request, 'mainPage.html')
    else:
        form = DescriptionForm()
        return render(request, 'resume_new.html', {"form": form})
