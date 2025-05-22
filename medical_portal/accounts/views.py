from django.shortcuts import render

from blog.models import BlogPost
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm, LoginForm
from .models import CustomUser

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print("Form errors:", form.errors)    
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if user.user_type == 'Patient':
                    return redirect('patient_dashboard')
                elif user.user_type == 'Doctor':
                    return redirect('doctor_dashboard')
            else:
            # Return login with error
                return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def patient_dashboard(request):
    user = request.user
    blog_posts = BlogPost.objects.filter(is_draft=False).order_by('-created_at')

    # Group blogs by category
    categories = {}
    for post in blog_posts:
        categories.setdefault(post.category, []).append(post)

    return render(request, 'patient_dashboard.html', {
        'user': user,
        'categories': categories,
    })


def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html', {'user': request.user})

def home_view(request):
    return render(request, 'home.html')
