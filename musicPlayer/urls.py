from django.urls import path
from . import views

urlpatterns = [
    path("",views.getIndexPage),
    path("user/view/",views.addProduct,name="addProduct")
]
