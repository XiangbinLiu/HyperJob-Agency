from django.urls import path
from django.views.generic import RedirectView
from . import views
urlpatterns = [
    path('', views.main_page),

    path('vacancies', views.VacanciesView.as_view()),
    path('signup', views.MySignupView.as_view()),
    path('login', views.MyLoginView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('home', views.home),
    path('home/', views.home),

    path('vacancies/new', views.vacancy_create),
    path('vacancy/new', views.vacancy_create),

    path('login/', RedirectView.as_view(url='/login')),
    path('logout/', RedirectView.as_view(url='/logout')),
    path('signup/', RedirectView.as_view(url='/signup')),
]
