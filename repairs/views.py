from django.shortcuts import render

def home(request):
    return render(request, 'repairs/home.html')

def services(request):
    return render(request, 'repairs/services.html')

def repair_detail(request, repair_id):
    # Здесь можно добавить логику для получения деталей ремонта по ID
    return render(request, 'repairs/repair_detail.html', {'repair_id': repair_id})

def contact(request):
    return render(request, 'repairs/contact.html')

def about(request):
    return render(request, 'repairs/about.html')
