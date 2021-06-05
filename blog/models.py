from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Category(models.Model):
    #category_id = models.CharField(max_length=10, primary_key=True)
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=False, null=False)

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify (self.category_name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '{}/{}/'.format('/blog', self.slug)


class Tags(models.Model):
    tag_id = models.CharField(max_length=20, primary_key=True)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return '{}/{}/'.format('/blog', self.slug)    


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.ForeignKey(User, on_delete= models.CASCADE, max_length= 200)
    status = models.IntegerField(choices=STATUS, default=0)
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '{}/{}/'.format('/blog', self.slug)


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

    def get_absolute_url(self):
        return '{}/{}/'.format('/blog', self.slug)


class Author(models.Model):
    author_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return '{}/{}/'.format('/blog', self.slug)


class BlogEntry (models.Model):
    entry_id = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=100)
    body = models.CharField(max_length=255)
    publication_date = models.DateTimeField('date published')
          

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '{}/{}/'.format('/blog', self.slug)
    


class CustomUser(User):
    gender_list = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]
    user_name = models.CharField(max_length=100)

    gender = models.CharField(max_length=2, choices=gender_list, default='Male')
    profile_pic = models.ImageField(upload_to='Media/profile_pics', blank=True)
    profile_desc = models.TextField(max_length=200)


    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return '{}/{}/'.format('/blog', self.slug)