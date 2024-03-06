from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from core.models import BlogPosts
from core.models import Contacts
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def index(request):
    #return HttpResponse('<h1>Hello this is my first website<h1/>')
    postss = BlogPosts.objects.all().order_by('-created_at')
    paginator = Paginator(postss, 9)
    page_number = request.GET.get("page",1)
    posts = paginator.get_page(page_number)
    count=len(postss)
    if(count%9==0):
        count=count//9
    else:
        count=count//9 + 1
    return render(request,'index.html', {'posts':posts, 
                                         'count':[i for i in range(1, count +1)],
                                         "n": len(postss),
                                         'page': int(page_number)})


def about(request):
    return render(request,'about.html',{})


def categories(request, category):
    postss = BlogPosts.objects.filter(category=category)
    paginator = Paginator(postss, 9)
    page_number = request.GET.get("page",1)
    posts = paginator.get_page(page_number)
    count=len(postss)
    if(count%9==0):
        count=count//9
    else:
        count=count//9 + 1
    return render(request,'categories.html',{'posts':posts, 
                                         'count':[i for i in range(1, count +1)],
                                         "n": len(postss),
                                         'category':category,
                                         'page': int(page_number)})
    # return render(request,'categories.html',{'posts':posts,'category':category})


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
    
        contact = Contacts.objects.create(name = name, email = email, subject = subject, message = message,)
        contact.save()
        messages.success(request, "Your message has been sent!")
        return redirect(index)
    return render(request,'contact.html',{})


@login_required(login_url='signin')
def addblog(request):
    if request.method == "POST":
        author = request.user
        image = request.FILES.get('blogImage')
        blog_title = request.POST['blogTitle']
        blog_description = request.POST['blogDescription']
        blog_category = request.POST['blogCategory']
        

        post = BlogPosts.objects.create(author = author,title = blog_title,
                                        description=blog_description,
                                        category = blog_category,
                                        image = image,
                                        )
        post.save()
        messages.success(request, "Your blog has been added!")
        return redirect(index)
    return render(request,'addblog.html',{})



def post(request,id):
    posts = BlogPosts.objects.get(id=id) 
    
    return render(request,'post.html',{'posts':posts})


def admin(request):
    return render(request)


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['cnfpassword']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email already exists')
                return redirect(index)
            
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username already exists')
                return redirect(index)
            else:
                user = User.objects.create_user(username = username, email=email, password=password)
                user.save()

                user_login  = auth.authenticate(username=username, password = password)
                auth.login(request, user_login)

                user_model = User.objects.get(username = username)
                messages.success(request, 'Sign up successfull')
                
                return redirect(setting)
        else:
            messages.info(request, "Passowrd not matching")
            return redirect(index)
    


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user  = auth.authenticate(username=username, password = password)

        if user is not None:
            #User is authenticated
            auth.login(request, user)
            messages.success(request, 'Sign in successfull')
            return redirect(index)
        else:
            
            messages.info(request, 'Username and/or Password is invalid')
            return redirect(index)
    else:
        return redirect(index)
    

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect(index)



def setting(request):
    return render(request,'setting.html')

