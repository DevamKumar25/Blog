from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect

from .models import Blog,Category

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
    context = {
        'single_blog' : single_blog,
    }
    return render(request,'blogs.html',context)


def search(request):
    keyword = request.GET.get('keyword')

    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description_icontains=keyword)| Q(blog_body_icontains=keyword), status='Published')
    context = {
        'blogs': blogs,
        'keyword': keyword,

    }
    return render(request,'search.html',context)
