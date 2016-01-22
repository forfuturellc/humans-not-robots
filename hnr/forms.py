from django import forms

class Uri(forms.Form):
	url=forms.URLField(label='Enter URL')
