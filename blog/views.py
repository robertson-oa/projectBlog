from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout



# Create your views here.
from django.views import generic
from .models import Author, Category, Post


from .forms import CommentForm,PostForm, CategoryForm,CreateUserForm,UserForm
from django.shortcuts import render, get_object_or_404


class PostList(generic.ListView):
    queryset = Post.objects.all().order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'




def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
        print('hello')
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})



    

def index(request):
    return render(request, 'blog/index.html')

def posts(request):
    return render(request, 'blog/post_detail.html')



###############################################
def home(request):
    categories_list = Category.objects.all()
    template = 'blog/home.html'
    context = {'categories': categories_list}
    return render(request, template, context)

def detail(request, slug):
    try:
        category = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'blog/detail.html', {'category': category})

def post(request):
    posts_list = Post.objects.all()
    template = 'blog/posts.html'
    context = {'post': posts_list}
    return render(request, template, context)

def post_details(request,slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Posts does not exist")
    return render(request, 'blog/post_detail.html', {'post': post})

def author(request):
    authors_list = Author.objects.all()
    template = 'blog/authors.html'
    context = {'authors': authors_list}
    return render(request, template, context)

def authors_details(request):
    HttpResponse('<h1>This is the authors details<h1/>')

def createblog_form(request):
    form = PostForm()
    template = 'blog/createpost_form.html'
    context = {'form':form}
    return render(request, template, context)

def category_form(request):
    form = CategoryForm()
    template = 'blog/category_form.html'
    context = {'form':form}
    return render(request, template, context)

    ############################################
def UserFormView(request):
    form = UserForm(request.POST)
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(request, "Account created for " + user)
        return redirect('login')
        form = UserForm()
    template = 'blog/userform.html'
    context = {'form':form}
    return render(request, template, context)

def Login(request):
    form = UserForm(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,"Username Or Password incorrect!")
    template = 'blog/loginform.html'
    context = {'form':form}
    return render(request, template, context)

def LogoutUser(request):
    logout(request)
    return redirect('login')



# def CreateUserFormView(request):
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#         form.save()
#         form = UserCreationForm()
#     template = 'blog/userform.html'
#     context = {'form':form}
#     return render(request, template, context)
