from django.db import models

from debtors.models.debtor_model import Debtor


class Debt(models.Model):
    description = models.CharField(max_length=155, null=False, blank=False, verbose_name="Descripción")
    debt = models.FloatField(null=False, blank=False, verbose_name="Deuda")
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE, related_name="debts", verbose_name="Deudor")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        db_table = "debts"
        verbose_name = "Deuda"
        verbose_name_plural = "Deudas"


    def __str__(self):
        return f'{self.description} - {self.debt} - {self.debtor.id}'