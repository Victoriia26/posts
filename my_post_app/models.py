from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post_image')

    def __str__(self):
        return f'{self.image.url}'

class Post(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    hashtag = models.ManyToManyField('Hashtag', related_name='hash_post')

    def __str__(self):
        return f'{self.name}'


class HashTag(models.Model):
    hash = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.hash}'
