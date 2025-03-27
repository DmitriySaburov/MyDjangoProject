from django.urls import path
from blog import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("user/<str:name>/<int:age>/", views.user),
    path("user/<str:name>/", views.user),
    path("user/", views.user),
]