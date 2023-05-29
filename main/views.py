from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse, JsonResponse,HttpResponseRedirect
from .models import Property,Agent
# Create your views here.
def home_page(request:HttpRequest):
    allProp = Property.objects.all().values()
    # print(allProp)
    allagents = Property.objects.all().values()
    return render(request, "index.html",{"props":allProp, "agents":allagents})

def about_page(request:HttpRequest):
    return render(request,"about.html")

def properties_page(request:HttpRequest):
    allProp = Property.objects.all().values()
    print(allProp)
    return render(request,"property-grid.html",{"props":allProp})

def pro_single(request:HttpRequest,id):
    return render(request,"property-single.html")

def contact_page(request:HttpRequest):
    return render(request,"contact.html")

def public_request(request:HttpRequest):
    if(request.method== 'POST'):
        print(request.POST['name'],request.POST['email'],request.POST['subject'],request.POST['message'])
        # 'name': ['samarjeet Singh Gautam'], 'email': ['test@example.com'], 'subject': ['sd'], 'message': ['sdsd']
        print("gettin datha")
        # print(request.body)
        return render(request,"contact.html")
    # return redirect('/contact')