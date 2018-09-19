from django.db import models

# Create your models here.

class Book(models.Model):
    STATES = [
        ('available', 'Available'),
        ('check-our', 'Check_out')
    ]
    title = models.CharField(max_length=48)
    author = models.CharField(max_length=48)
    year = models.CharField(max_length=48)
    status = models.CharField(choices=STATES, default='available', max_length=48)
    date_added = models.DateTimeField(auto_now_add=True)
    date_borrowed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Book: {self.title} ({self.status})'

    def __repr__(self):
        return f'Book: {self.title} ({self.status})'