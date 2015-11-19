from django.shortcuts import render
from .models import url

from .forms import uri

def home(request):
	#print 'REQUEST IS:',request

	form=uri()
	context={'form':form}
	template="home.html"
	return render(request,template,context)

def contributors(request):
	form=uri(request.POST or None)

	if form.is_valid():
		#print 'IS HERE:',form.cleaned_data
		print form.cleaned_data['url']
		data=url(form.cleaned_data['url'])


	context={'data':data}
	template="inhuman.html"
	return render(request,template,context)

