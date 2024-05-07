from django.db import models

# Create your models here.
class Siswa(models.Model):
    nama = models.CharField(max_length=255)
    tanggal_lahir = models.DateField()
    alamat = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=255)
    nilai_ujian = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

class Sekolah(models.Model):
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

class Pendaftaran(models.Model):
    nama = models.CharField(max_length=255)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    nomor_telepon = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nama