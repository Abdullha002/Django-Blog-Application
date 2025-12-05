from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Blogs, Category, Comment

def posts_by_category(request, category_id):
    posts = Blogs.objects.filter(status='published', category = category_id)
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts' : posts,
        'category' : category
    }

    return render(request, "post_by_category.html", context)

def blogs(request, slug):
    single_post = get_object_or_404(Blogs, slug=slug, status='published')
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.blog = single_post
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)
        # return redirect('blogs', slug=single_post.slug)
    comments = Comment.objects.filter(blog=single_post)
    comment_count = comments.count()
    context = {
        'single_post': single_post,
        'comments' : comments,
        'comment_count' : comment_count
    }
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blogs.objects.filter(title__icontains=keyword)
    context = {
        'blogs': blogs,
        'keyword': keyword
    }
    return render(request, "search.html", context)

