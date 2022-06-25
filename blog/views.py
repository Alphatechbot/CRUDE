from django.shortcuts import render
from django.views.generic.edit import  CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from .models import Post
from django.urls import  reverse_lazy


class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy
    template_name = 'base.html'


class PostListView(ListView):
    model = Post
    template_name = 'list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'


class PostDeleteView(DeleteView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy
    template_name = 'delete.html'


class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy






