# forms.py
from django import forms

class ProdutoForm(forms.Form):
    link = forms.URLField(
        label='Link do Produto',
        required=True,
        widget= forms.URLInput(attrs={"class": "form-control", "placeholder": "www.leroy.com.br"}))
