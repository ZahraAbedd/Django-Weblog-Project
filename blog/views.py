from django.views import generic
from django.urls import reverse_lazy

from .models import Post
from .Forms import PostForm

class PostListView(generic.ListView):
    # Go to model post and get everything then put in posts_list then send to template
    # Post.objects.all()
    model = Post
    # send to this template
    template_name = 'blog/posts_list.html'
    # Put data in this variable
    context_object_name = 'posts_list'
    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')         

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'

class PostUpdateView(generic.UpdateView):
    model = Post
    form_class =  PostForm
    template_name ='blog/post_create.html'

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name= 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list')

    # def get_success_url(self):
    #     return reverse('posts_list')


# def post_list_view(request):
#     # posts_list = Post.objects.all()
    # posts_list = Post.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'blog/posts_list.html', {'posts_list': posts_list})

# def post_detail_view(request, pk):
#     try:
#         post = Post.objects.get(pk = pk)
#     # except Post.DoesNotExist:
#     except ObjectDoesNotExist:
#         post = None
#         print('Excepted')
#     return render(request, 'blog/post_detail.html', {'post': post})

# def post_create_view(request):
#     if request.method == 'POST':
#         user_form = PostForm(request.POST)
#         if user_form.is_valid():
#             user_form.save()
#             return redirect('posts_list')
#     else:
#         user_form = PostForm()
#     return render(request, 'blog/post_create.html', context={'form': user_form})

# /blog/10/update
# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect('posts_detail',pk=pk)
#     return render(request, 'blog/post_create.html', context={'form': form})

# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('posts_list')
#     return render(request, 'blog/post_delete.html', context={'post': post})
