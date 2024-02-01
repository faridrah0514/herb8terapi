from django.db import models
import secrets

class Registration(models.Model):
    GENDER_CHOICES = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    ]

    RELIGION_CHOICES = [
        ('Islam', 'Islam'),
        ('Kristen', 'Kristen'),
        ('Katolik', 'Katolik'),
        ('Hindu', 'Hindu'),
        ('Budha', 'Budha'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('Menikah', 'Menikah'),
        ('Belum Menikah', 'Belum Menikah'),
    ]

    HERB8_INFO_CHOICES = [
        (0, 'Keluarga / Teman'),
        (1, 'Brosur / Koran'),
        (2, 'Spanduk / Baliho'),
        (3, 'Facebook'),
        (4, 'Instagram'),
        (5, 'Lainnya'),
    ]

    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    religion = models.CharField(max_length=10, choices=RELIGION_CHOICES, blank=True, null=True)
    marital_status = models.CharField(max_length=15, choices=MARITAL_STATUS_CHOICES)
    birth_date = models.DateField(blank=True, null=True)
    birth_place = models.CharField(max_length=100, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    diagnose = models.CharField(max_length=100, blank=True, null=True)
    had_surgery = models.BooleanField(blank=True, null=True, choices = [(True, 'Ya'), (False, 'Tidak')])
    herb8_info = models.IntegerField(choices=HERB8_INFO_CHOICES, blank=True, null=True)
    rand_id = models.CharField(max_length=16, default=secrets.token_hex(8))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
