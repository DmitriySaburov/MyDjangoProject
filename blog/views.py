# from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Главная</h2>")

def about(request):
    return HttpResponse("<h2>О сайте</h2>")

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def user(request, name="Неизвестно", age="Неизвестно"):
    return HttpResponse(f"<h2>Имя: {name}</h2><br><p>Возраст: {age}</p>")
