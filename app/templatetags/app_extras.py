from django.template.defaultfilters import stringfilter
from django import template
import time

register = template.Library()




"""
Generate CSS class based on data e.g. status tags etc
"""
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
"""
Generate CSS class based on data e.g. status tags etc
"""  
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
    





"""
Convert epoch time to date and time
"""
@register.simple_tag
def epoch_to_datetime(epoch):
	return time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(float(epoch)))

