from django.db import models
import os

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text[:50]}..."



class Book(models.Model):
    """Book model"""
    
    #Ratings
    Rating_CHOICES = (
        (1, 'Poor'),
        (2, 'Average'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent')
    )

    
    title = models.CharField(max_length= 200)
    date_added = models.DateTimeField(auto_now_add=True)
    book_image = models.ImageField(upload_to= 'images/')
    amazon_link = models.URLField(max_length=200, db_index=True, unique=True, blank=True)
    summary_field = models.TextField(max_length=300)
    rating = models.IntegerField(choices=Rating_CHOICES, default=1)
    
    class Meta:
        verbose_name_plural = 'books'

    def __str__(self):
        return f"{self.title}"
    
