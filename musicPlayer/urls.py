from django.urls import path
from . import views

urlpatterns = [
    path("",views.getIndexPage,name="home"),
    path("user/view/",views.addProduct,name="addProduct"),
    path("product/delete/<str:id>",views.deleteProduct,name="deleteProduct"),
    path("product/edit/<str:id>",views.editProduct,name="editProduct")
]
