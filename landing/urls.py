from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("group/<int:pk>", views.group, name="group"),
    path("processed/group/<int:pk>", views.ajaxHandler, name="processed"),
    # path("processed/group/<int:pk>", views.AjaxHandlerView.as_view(), name="processed"),

]