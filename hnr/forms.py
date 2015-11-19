from django import forms

class Uri(forms.Form):
	url=forms.CharField(label='Enter URL')
