from django.urls import path
from expense_tracker import views

urlpatterns = [
    #path('home/', views.home),
    path('dashboard/', views.dashboard),
    path('loginview/', views.login_view, name="loginview"),
    path('registrationview/', views.registration_view),
]