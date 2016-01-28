from django.db import models
import argparse
#import humanstxt

#regexlib.com/Search.aspx?k=url&AspxAutoDetectCookieSupport=1
#if website not available heroku returns empty dict

class Humans(models.Model):
	twitter=models.URLField(unique=True)
	name=models.CharField(max_length=70)
	role=models.CharField(max_length=100)
	site=models.URLField(null=True,default=None)
	
	timetsamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	updated=models.DateTimeField(auto_now_add=False,auto_now=True)
	
	def __unicode__(self):
		return self.twitter

class SubmitedUrls(models.Model):
	site=models.URLField(unique=True)
	site_humans=models.ManyToManyField(Humans)

	def __unicode__(self):
		return self.site



