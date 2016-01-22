
import re
import json
import urllib
import urlparse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Humans,SubmitedUrls
from django.template import RequestContext,loader
from .forms import Uri


def home(request):

	form=Uri(request.POST or None)
	context={'form':form}
	template="index.html"
	return render(request,template,context)

def humans(request):
	form=Uri(request.POST or None)
	data=[]
	template=loader.get_template('inhuman.html')

	if form.is_valid():
		human_url=url_parser(form.cleaned_data['url'])
		if human_url:
				url_obj,created=SubmitedUrls.objects.get_or_create(site=human_url)
				if created:
					human_data=call_herokuapp(human_url)
					print human_data
					if human_data != {}:
						if 'team' in human_data and len(human_data['team'])>0:
							for individual_dict in human_data['team']:
								try:
									human_obj,success=Humans.objects.get_or_create(twitter=individual_dict['twitter'],name=individual_dict['name'],role=individual_dict['role'],site=individual_dict['site'])
									human_obj.submitedurls_set.add(url_obj)
								except:
									return HttpResponse('Incomplete data about Human')
							data=url_obj.site_humans.all()
						else:
							return HttpResponse('No humans present on website')
						
					else:
						return HttpResponse('Website not available or no human-data available on that website')
				else:
					data=url_obj.site_humans.all()
					print data
					print type(data)
			
		else:
			return HttpResponse('Website not found')
			#return render(request,'hnr/error.html',{'error':'404 Website Not Found '})
				
	context={'data':data}
	#context=RequestContext(request,{'humans_list':data,})
	#return render(request,template,context)
	return HttpResponse(template.render(context))


def url_parser(s):
	pat=re.compile('^(http|https|ftp)\://[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(:[a-zA-Z0-9]*)?/?([a-zA-Z0-9\-\._\?\,\'/\\\+&amp;%\$#\=~])*$')
	pat2=re.compile('[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(:[a-zA-Z0-9]*)?/?([a-zA-Z0-9\-\._\?\,\'/\\\+&amp;%\$#\=~])*$')

	human_url=None

	if re.match(pat,s) or re.match(pat2,s):
		parsed=urlparse.urlparse(s)
		if parsed.scheme == 'https' :
			db_url=parsed.netloc
			human_url=parsed.netloc+'?use_ssl=true'
			return db_url
			
		elif parsed.scheme == 'http':
			human_url=parsed.netloc
			return human_url

		elif parsed.path != '' and parsed.scheme =='':
			human_url=parsed.path
			return human_url
	else:return False		

def call_herokuapp(human_url):
	#heroku returns a blank dictionary when resources not found
	try:
		f=urllib.URLopener().open('https://humans.herokuapp.com/'+human_url)
		data=json.loads(f.read())
		return data
	except:
		return {}


