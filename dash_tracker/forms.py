from django import forms

from .models import ProductItem

class ProductItemForm(forms.ModelForm):

    class Meta:
        model = ProductItem
        fields = ('date', 'meal', 'ingradient', 'quantity','mesurement',)
