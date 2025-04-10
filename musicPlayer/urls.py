from django.urls import path
from . import views

urlpatterns = [
    path("",views.getIndexPage,name="home"),
    path("user/view/",views.addProduct,name="addProduct"),
    path("product/delete",views.deleteProduct,name="deleteProduct")
]
