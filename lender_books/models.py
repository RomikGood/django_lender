from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver


class Book(models.Model):
    STATES = [
        ('available', 'Available'),
        ('unavailable', 'Unavailable')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')

    title = models.CharField(max_length=48)
    author = models.CharField(max_length=48)
    year = models.CharField(max_length=48)
    status = models.CharField(choices=STATES, default='available', max_length=48)
    date_added = models.DateTimeField(auto_now_add=True)
    date_borrowed = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Book: {self.title} ({self.status})'

    def __repr__(self):
        return f'Book: {self.title} ({self.status})'


@receiver(models.signals.post_save, sender=Book)
def set_book_borrowed_date(sender, instance, **kwargs):
    if instance.status == 'unavailable' and not instance.date_borrowed:
        instance.date_borrowed = timezone.now()
        instance.save()

