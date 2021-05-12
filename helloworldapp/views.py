from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def helloworld_views(request):
 #return HttpResponse('Hello World!')
 return render(request, 'helloworldapp/index.html')