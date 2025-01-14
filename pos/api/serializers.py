from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from pos_app.models import User, TablePasien, TableDokter, TableAntrian

class TablePasienSerializers(serializers.ModelSerializer):
    class Meta:
        model = TablePasien
        fields = ('id', 'nama', 'umur', 'gender', 'alamat', 'no_telp', 'email')


class TableDokterSerializers(serializers.ModelSerializer):
    class Meta:
        model = TableDokter
        fields = ('id', 'nama', 'no_telp', 'email')


class GetTableAntrianSerializers(serializers.ModelSerializer):
    # pasien = TablePasienSerializers(read_only=True)
    # dokter = TableDokterSerializers(read_only=True)

    class Meta:
        model = TableAntrian
        fields = ('id', 'no_antrian', 'status_antrian', 'created_on', 'pasien', 'dokter')


class TableAntrianSerializers(serializers.ModelSerializer):
    pasien = serializers.PrimaryKeyRelatedField(queryset=TablePasien.objects.all())
    dokter = serializers.PrimaryKeyRelatedField(queryset=TableDokter.objects.all())
    created_on = serializers.DateTimeField(read_only=True)

    class Meta:
        model = TableAntrian
        fields = ('id', 'no_antrian', 'status_antrian', 'created_on', 'pasien', 'dokter')


class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        # Autentikasi dengan model User kustom
        user = authenticate(username=username, password=password)
        
        if user is None:
            raise serializers.ValidationError("Username atau Password salah.")

        # Dapatkan atau buat token
        token, created = Token.objects.get_or_create(user=user)

        # Kirimkan token sebagai bagian dari data yang valid
        data['token'] = token.key
        return data