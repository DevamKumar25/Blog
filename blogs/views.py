from django.http import HttpResponse
from django.shortcuts import render

from .models import Blog

# Create your views here.

def posts_by_category(request,category_id):
    # fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status='Published',category=category_id)
    return HttpResponse(posts)