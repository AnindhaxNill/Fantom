from posts.models import *
from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView,CreateView
from .forms import PostCreatioForm


# Create your views here.

class IndexView(ListView):
    template_name = "posts/index.html"
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context ['slider_posts'] = Post.objects.all().filter(slider_post= True)
        return context


class PostDetail(DetailView):
    template_name ="posts/detail.html"
    model = Post
    context_object_name = 'single'

    def get_context_data(self, **kwargs):
        context = super(PostDetail,self).get_context_data(**kwargs)
        context ["slider_posts"]=Post.objects.all().filter(slider_post=True)
        
        return context
        

class CategoryDetail(ListView):
    model =Post
    template_name = "categories/category_detail.html"
    context_object_name = 'posts'
    def get_queryset(self):
        self.category = get_object_or_404(Category,pk=self.kwargs['pk'])
        return Post.objects.filter(category=self.category).order_by('-id')
    

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail,self).get_context_data(**kwargs)
        self.category = get_object_or_404(Category,pk=self.kwargs['pk'])
        context['category']=self.category
        return context


class TagDetail(ListView):
    model =Post
    template_name = "tags/tag_detail.html"
    context_object_name = 'posts'
    def get_queryset(self):
        self.tag = get_object_or_404(Tag,pk=self.kwargs['pk'])
        return Post.objects.filter(tag=self.tag).order_by('-id')
    

    def get_context_data(self, **kwargs):
        context = super(TagDetail,self).get_context_data(**kwargs)
        self.category = get_object_or_404(Tag,pk=self.kwargs['pk'])
        context['tag']=self.tag
        return context


class PostCreationView(CreateView):
    model = Post
    template_name = "posts/create_post.html"
    form_class = PostCreatioForm
