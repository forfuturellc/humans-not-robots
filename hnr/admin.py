from django.contrib import admin
from .models import Humans,SubmitedUrls

# Register your models here.
class URLAdmin(admin.ModelAdmin):
		model=SubmitedUrls

class HumansAdmin(admin.ModelAdmin):
	list_display=['__unicode__','twitter','role']
	#inlines=[URLAdmin,]
		
admin.site.register(Humans,HumansAdmin)
admin.site.register(SubmitedUrls,URLAdmin)
