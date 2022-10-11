from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Post, Category
from . forms import PostForm, EditForm

# Note: decorators for function-based views, mixin for class-based views to 
# require login
class PostView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/blog.html'
    ordering = ['-date_created']
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostView, self). get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetailView, self). get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class AddCategoryView(LoginRequiredMixin, CreateView):
    model = Category    
    template_name = 'blog/add_category.html'
    fields = '__all__'
    success_url = reverse_lazy('add_category')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self). get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


# idea for pagination for function views and for the templates from 
# https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
# for class based view and template, Corey Schafer youtube
@login_required
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' ')).order_by('-date_created')
    page = request.GET.get('page', 1)
    paginator = Paginator(category_posts,5) 
    try:
        category_posts = paginator.page(page)
    except PageNotAnInteger:
        category_posts = paginator.page(1)
    except EmptyPage:
        category_posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/categories.html', {'cats':cats.replace('-', ' '), 'category_posts':category_posts})

@login_required
def AuthorView(request, author):
    author_posts = Post.objects.filter(author=author).order_by('-date_created')
    author = User.objects.get(id=author)
    page = request.GET.get('page', 1)
    paginator = Paginator(author_posts, 5) 
    try:
        author_posts = paginator.page(page)
    except PageNotAnInteger:
        author_posts = paginator.page(1)
    except EmptyPage:
        author_posts = paginator.page(paginator.num_pages)
    
    return render(request, 'blog/author.html', {'author':author, 'author_posts':author_posts})


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/update_post.html'
    
    
class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog_home')


