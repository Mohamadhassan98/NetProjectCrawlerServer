from django.contrib import admin
from django.urls import path
from Crawler.views import *

urlpatterns = [
    path('', crawl, name='crawl'),
]