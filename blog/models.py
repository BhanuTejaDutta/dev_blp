from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    description= models.TextField()
    img=models.ImageField(upload_to='blog/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return self.title
