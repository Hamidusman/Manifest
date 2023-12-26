from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Blogpost
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

def main(request):
    blogposts = Blogpost.objects.all()
    categories = set([bp.category for bp in blogposts if bp.category])

    category_counts = {}
    for category in categories:
        category_name = dict(Blogpost.category.field.choices)[category]
        category_counts[category_name] = {
            'count': Blogpost.objects.filter(category=category).count(),
            'name': category_name,
        }

    context = {
        'blogposts': blogposts,
        'category_counts': category_counts,
    }

    return render(request, 'main.html', {'blogposts': blogposts, 'category_counts': category_counts})

def story(request, pk): 
    story = Blogpost.objects.get(id=pk)
    context = {'story': story}
    return render(request, 'story.html', {'story': story})