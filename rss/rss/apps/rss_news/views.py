from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rss.apps.rss_news.models import Post

# Create your views here.


def index(request):

    posts = reversed(Post.objects.all())

    context = {
        'posts': posts

    }

    return render(request, "index.html", context)


def post(request, index):

    try:
        post = Post.objects.get(id=index)
        previous_id = post.id - 1
        next_id = post.id + 1
        context = {
            'post': post,
            'previous_id': previous_id,
            'next_id': next_id,
            'max_id': len(Post.objects.all())
        }
        return render(request, "post.html", context)
    except Post.DoesNotExist:
        return render(request, "error_page.html")

def login(request):
    return render(request, "login.html")

def login_user(request):

    reg_user_name = request.POST["reg1user"]
    reg_password = request.POST["reg1password"]

    print(reg_user_name, reg_password)
    return HttpResponseRedirect('/')

def signup(request):
    return render(request, "signup.html")

def signup_user(request):

    user_name = request.POST["user_name"]
    password = request.POST["password"]
    repeat_password = request.POST["repeat_password"]
    email = request.POST["email"]


    print(user_name, password, repeat_password, email)

    return HttpResponseRedirect('/')

def error_page(request):
    return render(request, "error_page.html")