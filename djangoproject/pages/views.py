from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): #*args, **kwargs
	print(args, kwargs)
	print(request.user)
#	return HttpResponse("<h1>Hello World</h1>") # string of HTML code
	return render(request,"home.html", {})
	
def contact_view(request, *args, **kwargs): #*args, **kwargs
	return render(request,"contact.html", {}) # string of HTML code

def about_view(request, *args, **kwargs): #*args, **kwargs
	my_context={
		"title":"this is about us",
		# "this_is_true": True,
		"my_number": 123,
		"my_list": [123,4242,312, "Abc"],
		"my_html":"<h1>hello my friend</h1>"
	}
	return render(request,"about.html", my_context) # string of HTML code

def social_view(request, *args, **kwargs): #*args, **kwargs
	return HttpResponse("<h1>Social Page</h1>") # string of HTML code