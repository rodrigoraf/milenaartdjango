from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")
    photo = models.ImageField(upload_to='products/', verbose_name="Foto")
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")

    def __str__(self):
        return self.name
