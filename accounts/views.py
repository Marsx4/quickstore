from django.shortcuts import render

def register(request):
    context={
        "title":"Registration"
    }
    return render(request,'register.htm',context)

