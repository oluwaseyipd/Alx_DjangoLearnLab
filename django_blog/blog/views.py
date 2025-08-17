from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm, CommentForm
from .models import Post, Comment

# Home VIew
def home(request):
    return render(request, 'blog/index.html')

# Register VIew
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created successfully! You can now login')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'blog/auth/register.html', {'form':form})


# Blog Home Feed
@login_required
def feeds(request):
    return render(request, 'blog/pages/feeds.html')



# Users Profile View
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile Updated successfully!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'blog/pages/profile.html', context)


# Blog Post Views
class PostListView(ListView):
    model = Post
    template_name = 'blog/pages/feeds.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-published_date']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/pages/post-detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model= Post
    fields = ['title', 'content']
    template_name = 'blog/pages/write-post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model= Post
    fields = ['title', 'content']
    template_name = 'blog/pages/write-post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/pages/delete-post.html'
    success_url = '/posts'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# COmment Views

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/pages/add_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['post_id']
        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/pages/edit_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/pages/delete_comment.html'

    def get_success_url(self):
        return self.object.post.get_absolute_url()

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False