from .models import QrCodePayment
from django import forms


class QrCodePaymentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = QrCodePayment
        fields = ['amount', 'password',]
