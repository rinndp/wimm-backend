from django.db import models

from users.models import CustomUser


class Creditor(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nombre del acreedor')
    credit = models.FloatField(blank=True, null=True, verbose_name='Crédito')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='creditors', unique=False, verbose_name='Usuario')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')

    class Meta:
        db_table = 'creditors'
        verbose_name = 'Acreedor'
        verbose_name_plural = 'Acreedores'

    def update_credit(self):
        from credits.models import Credit
        credits_from_creditor = Credit.objects.filter(creditor=self).all()
        total_credit = 0
        for credit_object in credits_from_creditor:
            total_credit += credit_object.credit
        self.credit = total_credit
        self.save()

    def __str__(self):
        return f'{self.name} - {self.credit} - {self.user.slug}'