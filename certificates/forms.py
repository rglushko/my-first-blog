from django import forms

class CertificateForm(forms.Form):
    serial_number = forms.CharField(max_length=100)
    pin = forms.CharField(max_length=100)