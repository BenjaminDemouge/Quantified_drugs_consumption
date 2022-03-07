from django import forms
# Create the FormName class

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget = forms.Textarea)