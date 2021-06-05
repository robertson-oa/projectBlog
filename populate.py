from blog.models import Category,Tags,Post,Author,BlogEntry
import csv
import django
from django.utils import timezone
import os




data = []
tag_list = []
Authors =  []

with open ('questions.csv', newline = '') as csvfile:
    spamreader = csv.reader(csvfile, delimiter = ',')
    for row in spamreader:
        data.append (row)

with open("Tags.csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for i in spamreader:
        tag_list.append(i)

with open("Authors.csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for i in spamreader:
        tag_list.append(i)

tag_list = tag_list[1:]

data = data [1:]

Authors = Authors [1:]

def create_blog(category, blog, lorem):
    c = Category.objects.create(category_name=category)
    c.save()

    for element in blog:
        b = Post.objects.create(category=c, title=blog, body=lorem, publication_date=timezone.now())
        b.save()


def create_tags(tagg):
    tags = Tags.objects.create(tag=tagg)
    tags.save()


def create_authors(firstName, lastName):
    A = Authors.objects.create(first_name=firstName, last_name=lastName)
    A.save()


def populate_blogs(data,tag_list,Authors):
    print("starting to run population script.....")
    for datapoint in data:
        t = datapoint[0:4]
        c = datapoint[4]
        l = datapoint[5]
        create_blog(category=c, blog=t, lorem=l)
    print ("Finished running script")

    for tag in tag_list:
        t = tag[0]

        create_tags(tag=t)

    for name in Authors:
        fn = name[0]
        ln = name[1]


    create_authors(firstName=fn, lastName=ln)
    
populate_blogs(data,tag_list,Authors)


