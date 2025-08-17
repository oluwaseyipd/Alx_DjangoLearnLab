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
@login_required
def add_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect('post-detail', pk=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/pages/add_comment.html', {'form': form, 'post': post})
    return redirect('post-detail', pk=self.post.pk)



def edit_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user == comment.author:
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                messages.success(request, 'Comment updated successfully!')
                return redirect('post-detail', pk=comment.post.id)
        else:
            form = CommentForm(instance=comment)
        return render(request, 'blog/pages/edit_comment.html', {'form': form, 'comment': comment})
    else:
        messages.error(request, 'You are not allowed to edit this comment.')
        return redirect('post-detail', pk=comment.post.id)


@login_required
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user == comment.author:
        post_id = comment.post.id
        comment.delete()
        messages.success(request, 'Comment deleted successfully!')
        return redirect('post-detail', pk=post_id)
    else:
        messages.error(request, 'You are not allowed to delete this comment.')
        return redirect('post-detail', pk=comment.post.id)