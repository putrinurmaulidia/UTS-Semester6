from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .models import Siswa, Sekolah, Pendaftaran
from .serializers import SiswaSerializer, SekolahSerializer, PendaftaranSerializer

# Create your views here.
@api_view(['GET', 'POST']) # decorator
@permission_classes([permissions.AllowAny])
def Siswa_list(request, format=None):

    if request.method == 'GET':
        Siswa = Siswa.objects.all()
        serializer = SiswaSerializer(Siswa, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SiswaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Siswa_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        Siswa = Siswa.objects.get(pk=pk)
    except Siswa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SiswaSerializer(Siswa)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SiswaSerializer(Siswa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Siswa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST']) # decorator
@permission_classes([permissions.AllowAny])
def Sekolah_list(request, format=None):

    if request.method == 'GET':
        Sekolah = Sekolah.objects.all()
        serializer = SekolahSerializer(Sekolah, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SekolahSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Sekolah_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        Sekolah = Sekolah.objects.get(pk=pk)
    except Sekolah.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SekolahSerializer(Sekolah)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SekolahSerializer(Sekolah, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Sekolah.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST']) # decorator
@permission_classes([permissions.AllowAny])
def Pendaftaran_list(request, format=None):

    if request.method == 'GET':
        Pendaftaran = Pendaftaran.objects.all()
        serializer = PendaftaranSerializer(Pendaftaran, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PendaftaranSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def Pendaftaran_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        Pendaftaran = Pendaftaran.objects.get(pk=pk)
    except Pendaftaran.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PendaftaranSerializer(Pendaftaran)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Pendaftaran(Pendaftaran, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Pendaftaran.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# view untuk produk dengan class base view
class ProdukList(APIView):
    """
    ini merupakan proses pengambilan data atau simpan data
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        produk = Produk.objects.all()
        serializer = ProdukSerializer(produk, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProdukSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProdukDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    parser_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Produk.objects.get(pk=pk)
        except Produk.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        produk = self.get_object(pk)
        serializer = ProdukSerializer(produk)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        produk = self.get_object(pk)
        serializer = ProdukSerializer(produk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        produk = self.get_object(pk=pk)
        produk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)