from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    #############################################
    path('blog/userform/', views.UserFormView, name = 'userform'),
    path('blog/login/', views.LogoutUser, name='login'),
    path('blog/logout/', views.Login, name='logout'),
    path('blog/category/', views.home, name='category'),
    path('blog/category/<slug>', views.detail, name='detail'),
    path('blog/post/', views.post, name='post_home'),
    path('blog/post/<slug>', views.post_details, name='posts_details'),
    path('blog/author/', views.author),
    path('blog/author/<slug>', views.authors_details),
    path('blog/post/new/', views.createblog_form, name='new_post'),
    path('blog/category/new/', views.category_form, name='new_category'),


]