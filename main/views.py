from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User

def blogfieldDisplay(request):

    """allBlogData=Blog.objects.all().order_by('-upload_date') 
    allTags=Blog.tags.through.objects.all()
    #for data in allTags:
        #print(data)
    object_list = Blog.objects.all().order_by('-title')
    paginator = Paginator(object_list,3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        data_list = paginator.page(page)
        print(data_list)
    except PageNotAnInteger:
        data_list = paginator.page(1)
    except EmptyPage:
        data_list = paginator.page(paginator.num_pages)
    #return render(request,'AdvancedWorks/category_list.html',{'page': page,'data_list': data_list,})
        
    return render(request,"main/blogField.html",{"BlogData":allBlogData,"tags":allTags,'page': page,'data_list': data_list})"""

    allTags=Blog.tags.through.objects.all()
    user_list = Blog.objects.all().order_by('-title')
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 3)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'main/blogField.html', { "tags":allTags,'users': users })





def authorData(request,author_id):
    #allAuthorData=Blog.objects.filter(author_id=author_id).order_by('-title') 
    object_list = Blog.objects.filter(author_id=author_id).order_by('-title') 
    paginator = Paginator(object_list,3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        data_list = paginator.page(page)
        print(data_list)
    except PageNotAnInteger:
        data_list = paginator.page(1)
    except EmptyPage:
        data_list = paginator.page(paginator.num_pages)
    #return render(request,'AdvancedWorks/category_list.html',{'page': page,'data_list': data_list,})
    return render(request,"main/authorRelatedBlog.html",{'page': page,'data_list': data_list})

def tagData(request,id):
    allTagData=Blog.objects.filter(tags=id) 
    
    #allTagData=id.blog_set.all()
    return render(request,"main/tagRelatedBlog.html",{"TagData":allTagData})

from django.contrib.auth import authenticate,login,logout
def checkauth(request):
    if request.POST:
        uname=request.POST.get("txtuname")
        pswd=request.POST.get("txtpswd")
        UserCheck=authenticate(username=uname,password=pswd)
        if UserCheck is not None:
            login(request,UserCheck)
            return redirect('main_app:home')
        else:
            return HttpResponse("Something Wrong")
    else:
        return render(request,"main/Login.html")

def home(request):
    if request.user.is_authenticated:
        author_data_all=Author.objects.all()
       
        email1=request.user.email
        #author_data=Author.objects.get(email=request.user.email)
       # author_data11=author_data.email
        #print(author_data11)
        if email1 not in author_data_all:
            author_data=Author.objects.get(email=request.user.email)
            author_blog=Blog.objects.filter(author=author_data)
            uname=request.user.username
            request.session["uname"]=uname
            return render(request,"main/Home.html",{"blogData":author_blog,"sdata":request.session["uname"]})
        else:
            viewer_data=User.objects.get(username=request.user.username)
            uname=request.user.username
            request.session["uname"]=uname
            return render(request,"main/userHome.html",{"viewData":viewer_data,"sdata":request.session["uname"]})
            
    else:
        return HttpResponse("Please Login")    

def Userlogout(request):
    logout(request)
    return redirect("main_app:login")


"""--->creating users using UserCreationForm

from django.contrib.auth.forms import UserCreationForm
def UserSignup(request):
    if request.POST:
        userformOb=UserCreationForm(request.POST)
        if userformOb.is_valid():
            userformOb.save()
            return HttpResponse("Data Saved")
    else:
        userformOb=UserCreationForm()
        return render(request,"main/UserRegistration.html",{"form":userformOb})
"""
from .forms import UserRegistrationForm
def UserSignup(request):
    if request.POST:
        userformOb=UserRegistrationForm(request.POST)
        if userformOb.is_valid():
            userformOb.save()
            return HttpResponse("Data Saved")
        else:
            print(userformOb.errors)
            return HttpResponse("Invalid")
    else:
        userformOb=UserRegistrationForm()
        return render(request,"main/UserRegistration.html",{"form":userformOb})