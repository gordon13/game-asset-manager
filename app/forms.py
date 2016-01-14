from django.forms import ModelForm

from app.models import Asset

class AssetForm(forms.ModelForm):
    class Meta:
    	model = Asset
    	exclude = ['id'] 

