from django.shortcuts import render

def index(request):
    data = {"age": 50}
    return render(request, 'blog/index.html', context=data)