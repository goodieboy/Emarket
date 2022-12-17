from django.db import models
from django.conf import settings
from .flutterwave import Flutterwave
import secrets


# Create your models here.
class Payment(models.Model):
    email = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return f'Payment: {self.amount}'

    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(25)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)

    def payment_verification(self):
        flutterwave = Flutterwave()
        status, result = flutterwave.payment_verification(self.amount, id=id)
        if status:
            if result['amount'] == self.amount:
                self.verified = True
            self.save()
        if self.verified:
            return True
        return False

