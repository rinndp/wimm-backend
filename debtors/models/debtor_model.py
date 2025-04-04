from django.db import models
from django.db.models import OneToOneField, ForeignKey

from users.models import CustomUser


class Debtor(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nombre del deudor')
    debt = models.FloatField(blank=True, null=True, verbose_name='Deuda')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='debtors', unique=False, verbose_name='Usuario')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

    class Meta:
        db_table = 'debtors'
        verbose_name = 'Deudor'
        verbose_name_plural = 'Deudores'

    def __str__(self):
        return f"{self.name} - {self.debt}"
