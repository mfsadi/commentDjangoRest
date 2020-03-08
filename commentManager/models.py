from django.db import models


class Post(models.Model):
    # title=models.models.CharField(max_length=50)
    # content=models.TextField()
    pass
    # def __str__(self):
    #     return self.id
    

class Comment(models.Model):
    commenter = models.CharField(max_length=50)
    content = models.TextField()
    commenter_email = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


    def get_commenter(self):
        return self.commenter
    # def __str__(self):
    #     return (self.post)
