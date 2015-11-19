from django.db import models
import re
import urlparse
import argparse
import urllib
#import humanstxt

#regexlib.com/Search.aspx?k=url&AspxAutoDetectCookieSupport=1

def url(s):
	'''Takea a url string,validates using re and recreate it to call humans.herokuap.com >>produces 
		json string which is returned as data:dict
	 '''
	pat=re.compile('^(http|https|ftp)\://[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(:[a-zA-Z0-9]*)?/?([a-zA-Z0-9\-\._\?\,\'/\\\+&amp;%\$#\=~])*$')
	pat2=re.compile('[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}(:[a-zA-Z0-9]*)?/?([a-zA-Z0-9\-\._\?\,\'/\\\+&amp;%\$#\=~])*$')

	human_url=None

	if re.match(pat,s) or re.match(pat2,s):
		print 'Match successful'

		parsed=urlparse.urlparse(s)
		if parsed.scheme == 'https' :
			human_url=parsed.netloc+'?use_ssl=true'
			
			print human_url
		elif parsed.scheme == 'http':
			human_url=parsed.netloc

		elif parsed.path != '' and parsed.scheme =='':
			human_url=parsed.path
			print human_url


		f=urllib.URLopener().open('https://humans.herokuapp.com/'+human_url)
		data=f.read()
	
		return data

	else:print 'Error'



if __name__ == '__main__':
	parser=argparse.ArgumentParser()
	parser.add_argument("url",help="Enter valid url",type=str)
	args=parser.parse_args()
	url(args.url)

