from django import forms

class KensakuForm(forms.Form):
    find = forms.CharField(label='探す',required=False)