from django.shortcuts import render

# Create your views here.

def index(request):
    context_dict = {'text':'hello world','number':100} #1-5-2020 Template filters lecture Level 4
    return render(request,'basic_app/index.html',context_dict)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')
