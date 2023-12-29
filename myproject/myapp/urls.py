from django.urls import path

from . import views
from about import views2

urlpatterns = [
    path("",views.vote,name="detail"),
    path("home/v1",views.detail,name="nono"),
    path("home/v2",views.results,name="no"),
    path("/about/")
]