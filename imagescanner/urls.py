#this is the specified webpage url
from django.conf.urls import url
from . import views

from .views import ocr_view,ocr_form_view

urlpatterns = [
    url(r'^$', ocr_form_view, name='ocr_form_view'),
    url(r'^ocr/$', ocr_view, name='ocr_view'),
]
