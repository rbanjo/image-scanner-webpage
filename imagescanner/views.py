#take url request and send http response
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.generic.base import View, TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os
from django.conf import settings
from PIL import Image, ImageFilter
from wand.image import Image as IMG
import pytesseract

# Create your views here.
class OcrFormView(TemplateView):
    template_name='ocr_form.html'
ocr_form_view = OcrFormView.as_view()

def get_string(name):
    img=Image.open(name)
    sharpened_image = img.filter(ImageFilter.SHARPEN)
    utf8_text = pytesseract.image_to_string(sharpened_image)
    utf8_text = str(utf8_text.encode('ascii', 'ignore'))
    return utf8_text

class OcrView(View):
    def post(self, request):
        if("pdf" not in str(request.FILES['image'])):
            utf8_text=get_string(request.FILES['image'])
            print(utf8_text)
        else:
            data=request.FILES['image']
            default_storage.save(data.name, ContentFile(data.read()))
            img=IMG(filename=data.name,resolution=200)
            img.save(filename='temp.jpg')
            utf8_text=get_string('temp.jpg')
            print(utf8_text)
        return JsonResponse({'utf8_text': utf8_text})



ocr_view = csrf_exempt(OcrView.as_view())