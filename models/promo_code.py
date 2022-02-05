from django.db import models


class PromoCode(models.Model):
    class Meta:
        db_table = 'billing_promo_code'

    cost = models.IntegerField()
    promo = models.CharField(max_lenght=64)
    code = models.CharField(max_lenght=64)
    is_used = models.BooleanField(default=False)

    owner = models.ForeignKey(
        'Account', on_delete=models.DO_NOTHING, related_name='promo_codes',
        null=True, default=None, blank=True
    )

    @staticmethod
    def generate_code():
        """Example: 'AbCd-EfGh-IjKl-MnOp-QrSt-UvWx-YzAb-CdEf-GhIj-KlMn-OpQr-StUv-WxYz'"""
        import string
        import random
        return '-'.join([''.join([random.choice(string.ascii_letters) for _ in range(4)]) for _ in range(13)]),

    def save(self, *args, **kwargs):
        super(PromoCode, self).save(*args, **kwargs)
        if not self.code:
            self.code = self.generate_code()
            self.save()

    def use(self, account) -> tuple[bool, str]:
        from billing.models import OperationReason

        if self.is_used:
            return False, 'Код уже активирован'
        elif self.owner and self.owner != account:
            return False, 'Этот промо-код принадлежит другому аккаунту'
        else:
            if not self.owner:
                self.owner = account
            self.is_used = True
            self.owner.add_operation(value=self.cost, reason=OperationReason.PROMO, details=self.code)
            self.save()
