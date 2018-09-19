from django.test import TestCase, RequestFactory
from .models import Book


class TestBookModel(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title='Best book', author='Brooks')
        Book.objects.create(title='blarp', author='wat stick')
        Book.objects.create(title='Gnarf', author='django')

    def test_book_titles(self):
        self.assertEqual(self.book.title, 'Best book')

    def test_book_detail(self):
        book = Book.objects.get(title='Gnarf')

        self.assertEqual(book.author, 'django')


class TestBookViews(TestCase):
    def setUp(self):
        self.request = RequestFactory()
        self.book_one = Book.objects.create(title='blarp', author='wat stick')
        self.book_two = Book.objects.create(title='Gnarf', author='django')

    def test_book_detail_view(self):
        from .views import book_detail_view
        request = self.request.get('')
        response = book_detail_view(request, f'{self.book_one.id}')
        self.assertIn(b'wat stick', response.content)

    def test_book_detail_status(self):
        from .views import book_detail_view
        request = self.request.get('')
        response = book_detail_view(request, f'{self.book_one.id}')
        self.assertEqual(200, response.status_code)