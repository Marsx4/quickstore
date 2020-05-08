from django.shortcuts import render

def site_home_view(request):
    context={
        "title":"Home"
    }
    return render(request,'site_home.htm',context)

def contact(request):
    context={
        "title":"Contact"
    }
    return render(request,'site_contact.htm',context)

def about(request):
    context={
        "title":"About"
    }
    return render(request,'site_about.htm',context)

def terms(request):
    context={
        "title":"Terms & Conditons"
    }
    return render(request,'site_terms.htm',context)