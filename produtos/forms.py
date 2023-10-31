# forms.py
from django import forms

class ProdutoForm(forms.Form):
    link = forms.URLField(label='Link do Produto', required=True)
