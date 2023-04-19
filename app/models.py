from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CommentModel(models.Model):
    title = models.CharField('TITLE', max_length=250)
    content = models.TextField('CONTENT', max_length=500)
    img = models.ImageField('Картинка', upload_to='comment/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class CommentFromUsers(models.Model):
    name = models.CharField('Name', max_length=100)
    content = models.TextField('Content', max_length=250)
    img = models.ImageField('Image', upload_to='comment_from_users/')
    work = models.CharField('Work', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Comment From User'
        verbose_name_plural = 'Comments From Users'


class TeamModel(models.Model):
    name = models.CharField('Name', max_length=50)
    work = models.CharField('Work', max_length=100)
    facebook = models.TextField('Facebook', max_length=100)
    twitter = models.TextField('Twitter', max_length=100)
    img = models.ImageField('Image', upload_to='employ/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Team Worker'
        verbose_name_plural = 'Team Workers'


class DesignModel(models.Model):
    icon = models.CharField('Icon', max_length=200)
    name = models.CharField('Name', max_length=100)
    about = models.TextField('About', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Design'
        verbose_name_plural = 'Designs'


class Cat(models.Model):
    category = models.CharField('category', max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"

    def __str__(self):
        return self.category

class Design_projectsModel(models.Model):
    img = models.ImageField('Image', upload_to='design_projects/')
    name = models.CharField('Name', max_length=100)
    category = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Design projects'
        verbose_name_plural = 'Design projects'
