from django.db import models
from .models import *
class Blog_category(models.Model):
    name=models.CharField("Enter blog name",max_length=30)

    def __str__(self):
        return self.name

class Tags(models.Model):
    name=models.CharField("Enter tag name",max_length=30)
    def __str__(self):
        return self.name

class Author_category(models.Model):
    name=models.CharField("Enter author category name",max_length=30)
    def __str__(self):
        return self.name

class Author(models.Model):
    name=models.CharField("Enter author name",max_length=30)
    contact=models.CharField("Enter contact number",max_length=30)
    email=models.EmailField("Enter email id",max_length=30)
    address=models.CharField(max_length=500)
    author_category=models.ForeignKey(Author_category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField("Enter title name",max_length=100)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    blog_category=models.ForeignKey(Blog_category,on_delete=models.CASCADE)
    content=models.TextField(max_length=2000, help_text="Enter you blog text here.")
    upload_date=models.DateTimeField("Enter upload date and time",max_length=50)
    tags=models.ManyToManyField(Tags)
    def __str__(self):
        return self.title