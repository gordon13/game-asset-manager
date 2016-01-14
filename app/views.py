from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from django.shortcuts import render

from models import Asset

class BaseView(TemplateView):
    template_name = "app/index.html"

    def get_assets(self):
        return Asset.objects.all()


class DashboardView(TemplateView):
	template_name = "app/index.html"

	def get_assets(self):
		return Asset.objects.all()




"""
Asset creation, updation and deletion forms
"""
class AssetCreate(CreateView):
    model = Asset
    fields = ['name', 'asset_type']
    success_url = reverse_lazy('index')

class AssetUpdate(UpdateView):
    model = Asset
    fields = ['name', 'asset_type']

class AssetDelete(DeleteView):
    model = Asset
    success_url = reverse_lazy('index')