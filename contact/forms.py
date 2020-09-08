"""Forms for Contact app """
from django import forms

class ContactForm(forms.Form):
    
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True)

    class Meta:
        fields = ["subject", "from_email", "message"]
