from django.db import models


class Account(models.Model):
    @property
    def balance(self) -> int:
        return getattr(self.operations.last(), 'balance', 0)

    def add_operation(self, value, reason, details):
        self.operations.create(
            value=value,
            balance=self.balance + value,
            reason=reason,
            details=details,
        )
