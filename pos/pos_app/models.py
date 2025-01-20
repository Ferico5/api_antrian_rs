from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class TablePasien(models.Model):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    nama = models.CharField(max_length = 200, null = False, blank = False)
    umur = models.IntegerField(null = False, blank = False)
    gender = models.CharField(max_length = 6, choices = gender_choices, default = 'Pria')
    alamat = models.CharField(max_length = 500)
    no_telp = models.CharField(max_length = 15, null = False, blank = False)
    email = models.EmailField(max_length = 255, unique = True)

    def __str__(self):
        return self.nama


class TableDokter(models.Model):
    nama = models.CharField(max_length = 200, null = False, blank = False)
    no_telp = models.CharField(max_length = 15, null = False, blank = False)
    email = models.EmailField(max_length = 255, unique = True)

    def __str__(self):
        return self.nama



class TableAntrian(models.Model):
    antrian_choices = (
        ('0', 'Sedang menunggu'),
        ('1', 'Sudah dipanggil'),
        ('2', 'Selesai'),
        ('3', 'Batal'),
    )

    no_antrian = models.CharField(max_length = 200, unique = True, null = False, blank = False, editable = False)
    status_antrian = models.CharField(max_length = 20, choices = antrian_choices, default = 'Sedang menunggu')
    created_on = models.DateTimeField(auto_now_add = True)
    pasien = models.ForeignKey(TablePasien, on_delete=models.CASCADE)
    dokter = models.ForeignKey(TableDokter, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.no_antrian:
            last_antrian = TableAntrian.objects.all().order_by('-created_on').first()

            if last_antrian and last_antrian.no_antrian.isdigit():
                self.no_antrian = str(int(last_antrian.no_antrian) + 1)
            else:
                self.no_antrian = '1'
        super().save(*args, **kwargs)


    def __str__(self):
        return self.no_antrian