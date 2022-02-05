from django.db import models


class Account(models.Model):
    def __str__(self):
        return f'id: {self.id}\tbalance: {self.balance}'

    @property
    def balance(self) -> int:
        return getattr(self.operations.first(), 'balance', 0)

    def add_operation(self, value, reason, details):
        self.operations.create(
            value=value,
            balance=self.balance + value,
            reason=reason,
            details=details,
        )
