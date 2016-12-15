from django import template
from django.core.urlresolvers import reverse, resolve

register = template.Library()

# Register your models here.

@register.simple_tag

def navactive(request, urls):
	if request.path in (reverse (url) for url in urls.split()):
		return "active"
	return ""