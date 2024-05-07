from rest_framework import serializers
from .models import Siswa, Sekolah, Pendaftaran

# buat kelas serializer
class SiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siswa
        fields = ["nama", "tanggal_lahir", "alamat", "nomor_telepon", "nilai_ujian"]

class SekolahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sekolah
        fields = ["nama", "alamat",]

class PendaftaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pendaftaran
        fields = ["nama", "tanggal_lahir", "jenis_kelamin", "alamat", "nomor_telepon"]