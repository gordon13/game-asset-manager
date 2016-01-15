from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.simple_tag
def asset_status_label_class(value):
	""" 
	Returns the bootstrap class needed to dispplay the correct label
	"""
	if value == 'in_progress':
		return 'label-primary'
	elif value == 'done':
		return 'label-success'
	elif value == 'to_be_deleted':
		return 'label-danger'
	else:
		return 'label-primary'
   
@register.simple_tag
def asset_type_label_class(value):
	""" 
	Returns the bootstrap class needed to dispplay the correct label
	"""
	if value == 'art':
		return 'label-primary'
	elif value == 'audio':
		return 'label-success'
	elif value == 'writing':
		return 'label-danger'
	else:
		return 'label-primary'
    