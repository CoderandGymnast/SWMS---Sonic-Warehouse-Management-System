from django import template

register = template.Library()

@register.filter
def index(arr, i):
	return arr[i]
