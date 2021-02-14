"""bhavcopy_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from bhavcopy.views import (autocomplete, get_record, get_stock_records,
                            get_latest_records)
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import include, path

vue_urls = [
        path('', lambda request: HttpResponse(render(request, 'vue_index.html'))),
        ]

api_urls = [
        path('autocomplete', autocomplete, name='autocomplete'),
        path('record', get_record, name='single_record'),
        path('records', get_stock_records, name='all_for_one'),
        path('', get_latest_records, name='latest_records')
        ]

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include(vue_urls)),
        path('api/', include(api_urls)),
        ]
