from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.template import RequestContext
from models import Asset

def dashboard(request):
    assets = Asset.objects.order_by('date')[:5]
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'assets':assets
        })
    )

def art_section(request):
    assets = Asset.objects.filter(asset_type='art').order_by('-date')[:5]
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'assets':assets
        })
    )

def audio_section(request):
    assets = Asset.objects.filter(asset_type='audio').order_by('-date')[:5]
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'assets':assets
        })
    )

def writing_section(request):
    assets = Asset.objects.filter(asset_type='writing').order_by('-date')[:5]
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'assets':assets
        })
    )

def code_section(request):
    assets = Asset.objects.filter(asset_type='code').order_by('-date')[:5]
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'assets':assets
        })
    )