from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Post
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
                message.info(request, 'username already taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in Exists')
                return redirect('register')

            else: 
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'Registration successful. You can now login.')
                return redirect('main')
        else:
            messages.info('Password dont match')
            return redirect('register')
    return render(request, 'register.html')

def publish(request):
    if request.method == 'POST':
        title = request.POST['title']
        category = request.POST['category']
        read = request.POST['read'] 
        author = request.user
        if title is None:
            messages.info(request, 'Title required')
            return redirect
        elif read is None:
            messages.info(request, 'Texts are required')
        else:
            post = Post.objects.create(author=author, title=title, category=category, read=read)
            post.save()
            return redirect('main')
    return render(request, 'publish.html')


 
def main(request):
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

    context = {
        'posts': posts,
        'category_counts': category_counts,
        'search_query': search_query,
    }

    return render(request, 'main.html', context)

def story(request, pk): 
    story = Post.objects.get(id=pk)
    context = {'story': story}
    return render(request, 'story.html', {'story': story})