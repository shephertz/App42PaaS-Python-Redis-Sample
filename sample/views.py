from django.shortcuts import render

# Create your views here.
from django.utils import simplejson
from django.template import RequestContext
from django.shortcuts import render_to_response
from sample.models import User
from django.core.cache import cache
from django.http import Http404,HttpResponseRedirect
import datetime
import random, string

def index(request):
    
	return render_to_response("index.html",context_instance=RequestContext(request))
	
def save(request):

		random_bytes = [random.randint(0, 0xFF) for i in range(32)]
		bytes =  ''.join(map(byte_to_base32_chr, random_bytes))
		user = "user-"+bytes
		cache.set(user,{"name" : request.POST['name'], "description" : request.POST['description'], "email" : request.POST['email']}, timeout=None)
		results = cache.keys("user-*")
		lists = []
		for e in results:
			lists.append(cache.get(e))
		return render_to_response("home.html", {"lists": lists,},context_instance=RequestContext(request))
		

def byte_to_base32_chr(byte):

		alphabet = string.lowercase + string.digits 
		return alphabet[byte & 31]

