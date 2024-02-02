from django.urls import path

from . import views

urlpatterns = [
    path("",views.vote,name="detail"),
    path("home/v1",views.detail,name="nono"),
    path("home/v2",views.results,name="no"),
   # path("test/account/<int:first>/<int:second>", views.test, name="test"),
   # path("test1/account/<int:first>", views.test1, name="test1"),
#    path("/about/")
]