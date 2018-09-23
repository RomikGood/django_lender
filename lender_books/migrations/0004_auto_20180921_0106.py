# Generated by Django 2.1.1 on 2018-09-21 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lender_books', '0003_book_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_borrowed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable')], default='available', max_length=48),
        ),
    ]