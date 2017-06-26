#take url request and send http response
from django.http import HttpResponse

# Create your views here.
def index(response):
   return HttpResponse("This is the image scanner page")