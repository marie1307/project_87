from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the home page.")

def about(request):
    return HttpResponse("Here you can get information about our website.")

def contact(request):
    return HttpResponse("This is our contact page.")

def website(request):
    return HttpResponse("This is our main website")

# def name(request):
#     return HttpResponse(f"Hello, {request}, HttpResponse")
