from django.db import models

# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=254)

    def __str__(self):
        return self.tag_name


class Category(models.Model):
    name = models.CharField(max_length=250)
    tag =models.ManyToManyField('Tag')

    def __str__(self):
        return self.name

class Blog(models.Model):
    blog_name = models.CharField(max_length=30)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    text = models.CharField(max_length=450)


    def __str__(self):
        return self.blog_name
