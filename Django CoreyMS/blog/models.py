from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # auto now add - sets to now when the post is created
    author = models.ForeignKey(User, on_delete=models.CASCADE) # on delete tells django what we want to do if
    # the user who created this post gets deleted / one (User) to many (Posts) relationship
    # models.CASCADE tells that we want to delete posts if the user is deleted
    
    # user = User.objects.filter(username='osvaldas').first()
    # user = User.objects.get(id=1)
    # Post.objects.all()

    # post = Post(title='SQL Post', content='Nice content', author_id = user.id) 
    # user.post_set - get all the posts written by a specific user user.post_set.all()
    # .modelname_set
    # user.post_set.create(title='Blog 3', content= 'Third Post Content!') no need to specify author this time

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


    # redirect will redirect to a specific rout
    # reverse will return full url to that route as a string and let the view handle the redirect