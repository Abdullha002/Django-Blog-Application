from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, Blogs, Comment
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, PostForm, UserForm, EditUserForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

@login_required(login_url='login')
def dashboard(request):
    user = request.user
    category_count = Category.objects.all().count()

    # Check if user is manager
    is_manager = user.groups.filter(name='Manager').exists()

    # Blog count
    if is_manager:
        # Manager sees all blogs
        blogs_count = Blogs.objects.count()
        comments_count = Comment.objects.all().count()
    else:
        # Editor sees only their blogs
        user_blogs = Blogs.objects.filter(author=user)
        blogs_count = user_blogs.count()
        comments_count = Comment.objects.filter(user=user).count()

    context = {
        'user' : user,
        'category_count' : category_count,
        'blogs_count' : blogs_count,
        'comments_count' : comments_count
    }
    return render(request, 'dashboards/dashboard.html', context)

# Categories Views

def categories(request):
    return render(request, 'dashboards/categories.html')

def add_categories(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm()
    context = {
        'form': form
    }
    return render(request, 'dashboards/add_categories.html', context)

def edit_categories(request, cat_id):
    category = get_object_or_404(Category, id=cat_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form' : form,
        'category' : category
    }
    return render(request, 'dashboards/edit_categories.html', context)

def delete_categories(request, cat_id):
    category = get_object_or_404(Category, id=cat_id)
    category.delete()
    return redirect('categories')

# Posts Views

def posts(request):
    user = request.user
    # Check if user is manager
    is_manager = user.groups.filter(name='Manager').exists()

    # Post count
    if is_manager:
        # Manager sees all posts
        user_posts = Blogs.objects.all()

    else:
        # Editor sees only their blogs
        user_posts = Blogs.objects.filter(author=user)
    context = {
        'user_posts' : user_posts
    }
    return render(request, 'dashboards/posts.html', context)

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify('title')
            post.save()
            return redirect('posts')
    else:
        form = PostForm()
    context = {
        'form' : form
    }
    return render(request, 'dashboards/add_post.html', context)

def edit_post(request, post_id):
    post = get_object_or_404(Blogs, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')

    form = PostForm(instance=post)
    context = {
        'form' : form,
        'post' : post
    }
    return render(request, 'dashboards/edit_post.html', context)

def delete_post(request, post_id):
    post = get_object_or_404(Blogs, id=post_id)
    post.delete()
    return redirect('posts')

# Users Views

def users(request):
    users = User.objects.all()
    context = {
        'users' : users
    }
    return render(request, 'dashboards/users.html', context)

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = UserForm()
    context = {
        'form' : form
    }
    return render(request, 'dashboards/add_user.html', context)

def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = EditUserForm(instance=user)
    context = {
        'form' : form,
        'user' : user
    }
    return render(request, 'dashboards/edit_user.html', context)

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('users')

def comments(request):
    user = request.user
    # Check if user is manager
    is_manager = user.groups.filter(name='Manager').exists()

    # Post count
    if is_manager:
        # Manager sees all posts
        comments = Comment.objects.all()

    else:
        # Editor sees only their blogs
        comments = Comment.objects.filter(user=user)

    context = {
        'comments': comments
    }
    return render(request, "dashboards/comments.html", context)


def delete_comment(request, com_id):
    comment = get_object_or_404(Comment, id = com_id)
    comment.delete()
    return redirect('comments')