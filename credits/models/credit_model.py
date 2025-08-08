from django.db import models

from creditors.models.creditor_model import Creditor


class  Credit(models.Model):
    description = models.CharField(max_length=155, null=False, blank=False, verbose_name="Descripción")
    credit = models.FloatField(null=False, blank=False, verbose_name="Credito")
    creditor = models.ForeignKey(Creditor, on_delete=models.CASCADE, related_name="credits", verbose_name="Creditor")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        db_table = "credits"
        verbose_name = "Credito"
        verbose_name_plural = "Creditos"

    def __str__(self):
        return f'{self.description} - {self.credit} - {self.creditor.id}'

