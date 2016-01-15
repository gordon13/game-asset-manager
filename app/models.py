from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db import models
from django import forms

from AssetManagementTool.settings import ASSET_TYPES, ASSET_STATUSES, REGEX_ALLOWED_NAME_CHARACTERS
from app import rules

class Asset(models.Model):
	name = models.CharField(max_length=100, null=False)
	asset_type = models.CharField(max_length=50, choices=ASSET_TYPES, null=False, default=ASSET_TYPES[0][0])
	status = models.CharField(max_length=50, choices=ASSET_STATUSES, null=False, default=ASSET_STATUSES[0][0])
	notes = models.CharField(max_length=500, blank=True)
	asset_location = models.CharField(max_length=500, null=True)
	date = models.DateField(auto_now=True)

	def clean(self): 
		if Asset.objects.filter(name=self.name).exists():
			raise forms.ValidationError('Asset name already in use. Use a different name')
		if not REGEX_ALLOWED_NAME_CHARACTERS.match(self.name):			
			raise forms.ValidationError('Asset name should only contain letters, numbers, underscores or hyphens')
		super(Asset, self).clean()

	def __unicode__(self):
		return self.name




@receiver(pre_save)
def pre_save_handler(sender, instance, *args, **kwargs):
    instance.full_clean()