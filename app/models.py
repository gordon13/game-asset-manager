from __future__ import unicode_literals
from django.db import models

from AssetManagementTool.settings import ASSET_TYPES

class Asset(models.Model):
	name = models.CharField(max_length=100)
	asset_type = models.CharField(max_length=50, choices=ASSET_TYPES)

	def __unicode__(self):
		return self.name
# Create your models here.
