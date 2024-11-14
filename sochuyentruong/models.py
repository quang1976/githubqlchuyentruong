from django.db import models

# Create your models here.

class NamHoc(models.Model):
    tennamhoc = models.CharField(verbose_name="Năm học", max_length=10, unique=True)
    
    def __str__(self):
        return f"{self.tennamhoc}"
