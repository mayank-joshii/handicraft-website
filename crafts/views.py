from django.shortcuts import render, redirect
from crafts.models import customDesign
from crafts.models import contactForm
# Create your views here.

def index(request):

    return render(request, 'index.html')

def gallary(request):
    context = {'success': False}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        design = request.POST.get('design')
        print(name, email)
        ins = customDesign(name=name, email=email, design=design)
        ins.save()
        context['success'] = True
    return render(request, 'Gallary.html', context)

def contact(request):
    context = {'success': False}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        descp = request.POST.get('descp')
        # print(userName, userEmail)
        instwo = contactForm(name=name, email=email, descp=descp)
        instwo.save()
        context = {'success': True}
    return render(request, 'contact.html', context)

def about(request):

    return render(request, 'about.html')