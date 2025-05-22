# blog/views.py
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

@login_required
def create_blog(request):
    if request.user.user_type.lower() != 'doctor':
        return redirect('home')

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('doctor_posts')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def doctor_posts(request):
    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'blog/doctor_posts.html', {'posts': posts})

@login_required
def patient_blog_view(request):
    categories = ['Mental Health', 'Heart Disease', 'Covid19', 'Immunization']
    category_posts = {
        cat: BlogPost.objects.filter(category=cat, is_draft=False) for cat in categories
    }
    return render(request, 'blog/patient_blogs.html', {'category_posts': category_posts})
def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, id=pk)
    return render(request, 'blog/blog_detail.html', {'post': post})
