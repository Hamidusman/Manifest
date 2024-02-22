from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import get_user_model
from .models import Post, Comment, Notification, Profile
from django.db.models import Q   
# Create your views here.

User = get_user_model()
def index(request):
    return render(request, 'index.html')


def register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                #messages.info(request, 'username already taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
               # messages.info(request, 'Email already in Exists')
                return redirect('register')

            else: 
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()

             #   messages.success(request, 'Registration successful. You can now login.')
                return redirect('login')
        else:
            messages.info('Password dont match')
            return redirect('register')
    return render(request, 'register.html')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None: 
            auth_login(request, user)
            return redirect('main') 
        else:

            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


def main(request):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    search_query = request.GET.get('q', '')
    posts = Post.objects.filter(
        Q(title__icontains=search_query) |
        Q(author__username__icontains=search_query) |
        Q(category__icontains=search_query)
    )
    categories = set([p.category for p in posts if p.category])

    category_counts = {}
    for category in categories:
        category_counts[category] = {
            'count': posts.filter(category=category).count(),
            'name': category,
        }

    notifications = Notification.objects.filter(user=request.user)

    context = {
        'posts': posts,
        'category_counts': category_counts,
        'search_query': search_query,
        'notifications': notifications,
        'profile' : user_profile,

    }

    return render(request, 'main.html', context)



def create_post(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        title = request.POST['title']
        picture = request.FILES['picture']
        category = request.POST['category']
        read = request.POST['read'] 
        if title is None:
            messages.info(request, 'Title required')
            return redirect
        elif read is None:
            messages.info(request, 'Texts are required')
        else:
            post = Post.objects.create(author = request.user, title=title, category=category, read=read, picture=picture, )
            post.save()
            return redirect('main')
    return render(request, 'publish.html', {'profile':profile})

def update_post(request, pk):
    post = Post.objects.get(id = pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        post.title = request.objects.POST.get('title')
        post.category = request.objects.POST.get('category')
        post.read =  request.objects.POST.get('read')
        post.save()
        return redirect('main')
    return render(request, 'publish.html', {'post': post})

def delete_post(request, pk):
    post = Post.objects.filter(id=pk)
    post.delete()
    return redirect('main')


def profile(request, pk):
    profile= Profile.objects.get(id=pk) 
    posts = Post.objects.filter(author = profile.user)
    post_count = posts.count()
    context = {'profile': profile, 'posts': posts, 'post_count': post_count }
    return render(request, 'profile.html', context)

def edit_profile(request, pk):
    profile = Profile.objects.get(user = request.user)
    context = {'profile': profile}
    return render(request, 'edit-profile.html', context)

'''def create_profile(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request..POST['lastname']
        about = request.POST['about']
        dob = request.POST['dob']
        phone = request.method['phone']
        picture = request.POST['picture']
        email = request.POST['email']

        profile = profile.'''

def story(request, pk):
    story = Post.objects.get(id=pk) 
    comments = Comment.objects.filter(post=story)
    p = Profile.objects.get(user = request.user)
    profile = Profile.objects.get(user = story.author)


    if request.method == 'POST' :
        comment = request.POST['comment']
        new_comment = Comment.objects.create(user = request.user, comment=comment, post=story)
        new_comment.save()
    context = {'story': story, 'comments': comments, 'p':p, 'profile':profile}
    return render(request, 'story.html', context)

def del_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return redirect('main') #need to rework on this
    