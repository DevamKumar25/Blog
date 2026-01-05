from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import Blog,Category,Comment

from django.db.models import Q
# Q is used to build complex database queries in Django.
# It lets you use OR, AND, and NOT conditions in filter() queries.

# Create your views here.

def posts_by_category(request,category_id):
    # fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status='Published',category=category_id)
    # try:
    #     category = get_object_or_404(Category,pk=category_id)
    # except :
    #     # redirect to the homepage
    #     return redirect('home')

    # Use get_object_or_404 when you want to show 404 error page if the category does not exit
    category = get_object_or_404(Category,pk=category_id)
    context = {
        'posts' : posts,
        'category' : category,
    }
    return render(request,'posts_by_category.html',context)


def blogs(request,slug):
    single_blog = get_object_or_404(Blog,slug=slug,status='Published')
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)  # Redirect to the same page after POST request

    #  comments
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()

    context = {
        'single_blog' : single_blog,
        'comments' : comments,
        'comment_count' : comment_count,
    }
    return render(request,'blogs.html',context)


def search(request):
    keyword = request.GET.get('keyword', '').strip() # Get the search keyword from the request and strip any leading/trailing whitespace

    blogs = []
    if keyword:
        blogs = Blog.objects.filter(
            Q(title__icontains=keyword) |
            Q(short_description__icontains=keyword) |
            Q(blog_body__icontains=keyword),
            status='Published'
        )

    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)