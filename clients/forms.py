from django import forms
from .models import Client,Transaction

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone_number']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['client', 'amount', 'transaction_type']
