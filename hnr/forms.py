from django import forms

class uri(forms.Form):
	url=forms.CharField(label='Enter URL')
