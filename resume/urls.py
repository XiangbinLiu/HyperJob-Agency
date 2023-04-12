from django.urls import path
from . import views
urlpatterns = [
    path('resumes', views.ResumesView.as_view()),
    path('resumes/new', views.resume_create),
    path('resume/new', views.resume_create),
]
