from django.shortcuts import render

def home(request):
    return render(request, 'mainecoon/home.html')

def page1(request):
    return render(request, 'mainecoon/page1.html')

def page2(request):
    return render(request, 'mainecoon/page2.html')

def page3(request):
    return render(request, 'mainecoon/page3.html')

def page4(request):
    return render(request, 'mainecoon/page4.html')
