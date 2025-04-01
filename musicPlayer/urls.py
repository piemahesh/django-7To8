from django.urls import path
from . import views

urlpatterns = [
    path("user/",views.getIndexPage),
    path("user/view/",views.gotoUserPage,name="user_view")
]
