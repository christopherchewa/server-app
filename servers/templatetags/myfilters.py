from django import template
register = template.Library()

# Register your models here.

@register.filter(name = 'addclass')

def addclass(value, arg):
	return value.as_widget(attrs={'class':arg})