from django.shortcuts import render
from django.views import View
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from gradesApp.models import Student,Teacher
from django.contrib.auth.models import User


class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()
        val = False

        try:
            current=Student.objects.get(student=request.user)
            val = current.is_student
        except Student.DoesNotExist:
            current=Teacher.objects.get(teacher=request.user)


        context = {
            'post_list': posts,
            'form': form,
            'is_student': val,
        }

        return render(request, 'Post/post_list.html', context)

    def post(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm(request.POST)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            form = PostForm(request.POST)
        val = False

        try:
            current=Student.objects.get(student=request.user)
            val = current.is_student
        except Student.DoesNotExist:
            current=Teacher.objects.get(teacher=request.user)

        context = {
            'post_list': posts,
            'form': form,
            'is_student':val,
        }

        return render(request, 'Post/post_list.html', context)




class PostDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()

        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'Post/post_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()

        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'Post/post_detail.html', context)
