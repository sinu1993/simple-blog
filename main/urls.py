
from django.contrib import admin
from django.urls import path
from main import views
app_name="main_app"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("blogview/",views.blogfieldDisplay,name="blogfieldDisplay"),
    path("authordataview/<str:author_id>/",views.authorData,name="authorData"),
    path("tagdataview/<str:id>/",views.tagData,name="tagData"),
    path("home/",views.home,name="home"),
    path("login/",views.checkauth,name="login"),
    path("logout/",views.Userlogout,name="Userlogout"),
    path("usersignup/",views.UserSignup,name="user-signup")
]
