from django.forms import ModelForm
from .models import Account, Transaction


# creates Account form based on account model
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


# creates transaction from based on transaction model
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

