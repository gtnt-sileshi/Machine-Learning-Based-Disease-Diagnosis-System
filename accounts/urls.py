from django.urls import path
from . import views

urlpatterns = [
    path('sign_in_patient', views.sign_in_patient , name='sign_in_patient'),
    path('signup_patient', views.signup_patient, name="signup_patient"),
    path('sign_in', views.sign_in , name='sign_in'),
    path('savepdata/<str:patientusername>', views.savepdata , name='savepdata'),
    path('signup_doctor', views.signup_doctor , name="signup_doctor"),
    path('saveddata/<str:doctorusername>', views.saveddata , name='saveddata'),
    path('logout', views.logout , name='logout'),
]