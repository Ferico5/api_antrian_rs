from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from pos_app.models import User, TablePasien, TableDokter, TableAntrian
from api.serializers import TablePasienSerializers, TableDokterSerializers, TableAntrianSerializers, GetTableAntrianSerializers, LoginSerializers
from rest_framework.authtoken.models import Token

class TablePasienListApiView(APIView):
    def get(self, request, *args, **kwargs):
        table_pasien = TablePasien.objects.all()
        serializer = TablePasienSerializers(table_pasien, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'nama' : request.data.get('nama'),
            'umur' : request.data.get('umur'),
            'gemder' : request.data.get('gemder'),
            'alamat' : request.data.get('alamat'),
            'no_telp' : request.data.get('no_telp'),
            'email' : request.data.get('email'),
        }

        serializer = TablePasienSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': status.HTTP_201_CREATED,
                'message': 'Data berhasil dibuat',
                'data': serializer.data
            }
            return Response(response, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class TablePasienDetailApiView(APIView):
    def get_id(self, id):
        try:
            return TablePasien.objects.get(id = id)
        except TablePasien.DoesNotExist:
            return None

    def id_not_found(self, id):
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': f'Tidak ada pasien dengan id {id}',
        })

    def get(self, request, id, *args, **kwargs):
        id_pasien = self.get_id(id)

        if not id_pasien:
            return self.id_not_found(id)

        serializers = TablePasienSerializers(id_pasien)

        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Data pasien berhasil didapatkan',
            'data': serializers.data
        })

    
    def put(self, request, id, *args, **kwargs):
        id_pasien = self.get_id(id)

        if not id_pasien:
            return self.id_not_found(id)

        data = {
            'nama': request.data.get('nama'),
            'umur': request.data.get('umur'),
            'gender': request.data.get('gender'),
            'alamat': request.data.get('alamat'),
            'no_telp': request.data.get('no_telp'),
            'email': request.data.get('email'),
        }

        serializers = TablePasienSerializers(instance = id_pasien, data = data, partial = True)

        if serializers.is_valid():
            serializers.save()

            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Data pasien berhasil diubah',
                'data': serializers.data,
            })


        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Data pasien gagal diubah',
            'errors': serializers.errors,
        })


    def delete(self, request, id, *args, **kwargs):
        id_pasien = self.get_id(id)

        if not id_pasien:
            return self.id_not_found(id)

        id_pasien.delete()

        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Data pasien berhasil dihapus',
        })


class TableDokterListApiView(APIView):
    def get(self, request, *args, **kwargs):
        table_dokter = TableDokter.objects.all()
        serializer = TableDokterSerializers(table_dokter, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'nama' : request.data.get('nama'),
            'no_telp' : request.data.get('no_telp'),
            'email' : request.data.get('email'),
        }

        serializer = TableDokterSerializers(data = data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status': status.HTTP_201_CREATED,
                'message': 'Data berhasil dibuat',
                'data': serializer.data
            }
            return Response(response, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class TableDokterDetailApiView(APIView):
    def get_id(self, id):
        try:
            return TableDokter.objects.get(id = id)
        except TableDokter.DoesNotExist:
            return None

    def id_not_found(self, id):
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': f'Tidak ada dokter dengan id {id}',
        })

    def get(self, request, id, *args, **kwargs):
        id_dokter = self.get_id(id)

        if not id_dokter:
            return self.id_not_found(id)

        serializers = TableDokterSerializers(id_dokter)

        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Data dokter berhasil didapatkan',
            'data': serializers.data
        })

    
    def put(self, request, id, *args, **kwargs):
        id_dokter = self.get_id(id)

        if not id_dokter:
            return self.id_not_found(id)

        data = {
            'nama': request.data.get('nama'),
            'no_telp': request.data.get('no_telp'),
            'email': request.data.get('email'),
        }

        serializers = TableDokterSerializers(instance = id_dokter, data = data, partial = True)

        if serializers.is_valid():
            serializers.save()

            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Data dokter berhasil diubah',
                'data': serializers.data,
            })


        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Data dokter gagal diubah',
            'errors': serializers.errors,
        })


    def delete(self, request, id, *args, **kwargs):
        id_dokter = self.get_id(id)

        if not id_dokter:
            return self.id_not_found(id)

        id_dokter.delete()

        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Data dokter berhasil dihapus',
        })


class TableAntrianListApiView(APIView):
    def get(self, request, *args, **kwargs):
        table_antrian = TableAntrian.objects.all()
        serializer = GetTableAntrianSerializers(table_antrian, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'status_antrian': request.data.get('status_antrian', 'Sedang menunggu'),
            'pasien': request.data.get('pasien'),
            'dokter': request.data.get('dokter'),
        }

        serializer = TableAntrianSerializers(data=data)
        
        if serializer.is_valid():
            table_antrian = serializer.save()

            response_data = GetTableAntrianSerializers(table_antrian)

            response = {
                'status': status.HTTP_201_CREATED,
                'message': 'Antrian berhasil dibuat',
                'data': response_data.data
            }

            return Response(response, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TableAntrianDetailApiView(APIView):
    def get_id(self, id):
        try:
            return TableAntrian.objects.get(id = id)
        except TableAntrian.DoesNotExist:
            return None

    def id_not_found(self, id):
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': f'Tidak ada antrian dengan id {id}',
        })

    def get(self, request, id, *args, **kwargs):
        id_antrian = self.get_id(id)

        if not id_antrian:
            return self.id_not_found(id)

        serializers = GetTableAntrianSerializers(id_antrian)

        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Data antrian berhasil didapatkan',
            'data': serializers.data
        })


    def delete(self, request, id, *args, **kwargs):
        id_antrian = self.get_id(id)

        if not id_antrian:
            return self.id_not_found(id)

        id_antrian.delete()

        return Response({
            'status': status.HTTP_200_OK,
            'message': 'Data antrian berhasil dihapus',
        })


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializers(data=request.data)
        
        if serializer.is_valid():
            return Response(
                {
                    'status': 'success',
                    'message': 'Login berhasil',
                    'token': serializer.validated_data['token']
                },
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            # Ambil token dari header Authorization
            token = request.auth  # `request.auth` adalah token yang digunakan oleh user yang terautentikasi

            # Hapus token untuk logout
            token.delete()

            return Response(
                {'message': 'Logout berhasil'},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {'message': 'Gagal melakukan logout', 'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )