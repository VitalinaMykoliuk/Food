from django.shortcuts import render


def index(request):
    return render(request, 'products/index.html')


def about(request):
    return render(request, 'products/about.html')


def news(request):
    return render(request, 'products/news.html')


def contact(request):
    return render(request, 'products/contact.html')


def recipes(request):
    return render(request, 'products/recipes.html')


def services(request):
    return render(request, 'products/services.html')


def single(request):
    return render(request, 'products/single.html')
