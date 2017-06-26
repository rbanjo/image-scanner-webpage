#take url request and send http response
from django.http import HttpResponse
from django.template import loader 

# Create your views here.
def index(response):
   all_uploads = uploads.objects.all()
   template = loader.get__template('image.scanner/index,html')
   context = {
      'all_uploads': all_uploads,
   }
   
   return HttpResponse(template.render(context, request)
   