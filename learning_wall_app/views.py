from django.http import HttpResponse,JsonResponse
from django.template import loader
from forms import PostForm ,RegisterForm,LoginForm
from models import User,Posts
from datetime import datetime
from django.shortcuts import redirect,render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.contrib.auth import login,authenticate,logout as django_logout
from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth.hashers import make_password

@login_required(login_url='login/')
def index(request):
    template = 'learning_wall_app/index.html'
    post_list=''
    if request.user.moderator == False:
        post_list=Posts.objects.filter(moderated=True).annotate(likes_count=Count('likes')).order_by('-likes_count')
    elif request.user.moderator == True:
        post_list=Posts.objects.all().annotate(likes_count=Count('likes')).order_by('-likes_count')
    paginator = Paginator(post_list,25) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    context={'posts':posts}
    return render(request,template,context=context)

#def post(request):
@csrf_exempt
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_body=form.cleaned_data['post_body']
            p=Posts(body=post_body,time=datetime.now(),user=request.user)
            p.save()
    return redirect('index')

    def like(request):
        p=Posts(body=post_body,time=datetime.now(),user=user)
        p.save()
    return redirect('index')

@csrf_exempt
def login_user(request):
    if request.method == 'GET':
        return render(request,'learning_wall_app/login.html')
    if request.method == 'POST':
        print request.POST.get('password')
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request,user)
        return redirect('index')

def logout(request):
    django_logout(request)
    return redirect('index')


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            print raw_password
            name = form.cleaned_data.get('name')
            print name+"**"
            User.objects.create(username=username, password=make_password(raw_password),name=name)
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'learning_wall_app/signup.html', {'form': form})

@csrf_exempt
@login_required
def like(request):
    if request.POST.get('type') == 'like':
        print "like received"
        post = Posts.objects.get(id=request.POST.get('id'))
        post.likes.add(request.user)
    elif request.POST.get('type') == 'unlike':
        print "unlike received"
        post = Posts.objects.get(id=request.POST.get('id'))
        post.likes.remove(request.user)

    return JsonResponse({"data":"hello"})

@csrf_exempt
def approve(request):
    post = Posts.objects.get(id=request.POST.get('id'))
    print "approve received"
    if post:
        post.moderated=True
        post.save()
        return JsonResponse({'data':'1'},status=200)
    else:
        return JsonResponse({'data':'1'},status=400)


@csrf_exempt
def reject(request):
    post = Posts.objects.get(id=request.POST.get('id'))
    print "reject received"
    if post:
        post.delete()
        return JsonResponse({'data':'1'},status=200)
    else:
        return JsonResponse({'data':'1'},status=400)






