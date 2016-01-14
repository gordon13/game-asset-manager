"""AssetManagementTool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from app.views import DashboardView, AssetCreate, AssetUpdate, AssetDelete

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', DashboardView.as_view(), name='index'),

    # asset creation, updation etc
    url(r'asset/add/$', AssetCreate.as_view(), name='asset-add'),
    url(r'asset/(?P<pk>[0-9]+)/$', AssetUpdate.as_view(), name='asset-update'),
    url(r'asset/(?P<pk>[0-9]+)/delete/$', AssetDelete.as_view(), name='asset-delete'),
]
