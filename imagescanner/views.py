#take url request and send http response
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.generic.base import View, TemplateView
from django.views.decorators.csrf import csrf_exempt
from PIL import Image, ImageFilter
import pytesseract

# Create your views here.
class OcrFormView(TemplateView):
    template_name='ocr_form.html'
ocr_form_view = OcrFormView.as_view()

class OcrView(View):
    def post(self, request):
        with Image.open(request.FILES['image']) as image:
                sharpened_image = image.filter(ImageFilter.SHARPEN)
                utf8_text=pytesseract.image_to_string(sharpened_image)
                print(utf8_text)
        return JsonResponse({'utf8_text': utf8_text})

ocr_view = csrf_exempt(OcrView.as_view())