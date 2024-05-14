from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('Siswa/', views.SiswaList.as_view()),
    path('Siswa/<int:pk>/', views.SiswaDetail.as_view()),
    path('Sekolah/', views.SekolahList.as_view()),
    path('Sekolah/<int:pk>/', views.SekolahDetail.as_view()),
    path('Pendaftaran/', views.PendaftaranList.as_view()),
    path('Pendaftaran/<int:pk>/', views.PendaftaranDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)