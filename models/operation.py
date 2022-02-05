from django.db import models

from safe_delete.models import SafeDeleteTextChoices


class OperationReason(SafeDeleteTextChoices):
    """Причина операции"""
    OTHER = 'OTHER', 'Прочее'
    FEE = 'FEE', 'Абонентская плата'
    PROMO = 'PROMO', 'Активация промо-кода'


class Operation(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField()
    balance = models.IntegerField()
    reason = OperationReason.field()
    details = models.CharField(max_lenght=255, blank=True)

    account = models.ForeignKey(
        'Account', on_delete=models.DO_NOTHING, related_name='operations',
        null=True, default=None, blank=True
    )

    class Meta:
        ordering = ('-time',)
