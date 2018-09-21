from django.test import TestCase, RequestFactory
from .models import Book
from django.contrib.auth.models import User


class TestBookModel(TestCase):
    def setUp(self):

        self.user = User.objects.create(username='test', email='test@gmail.com')
        self.user.set_password('test')

        self.book = Book.objects.create(
            title='Best book',
            author='Brooks',
            user=self.user)
        Book.objects.create(title='blarp', author='wat stick', user=self.user)
        Book.objects.create(title='Gnarf', author='django', user=self.user)
        
    def test_book_titles(self):
        self.assertEqual(self.book.title, 'Best book')

    def test_book_detail(self):
        book = Book.objects.get(title='Gnarf')
        self.assertEqual(book.author, 'django')


class TestBookViews(TestCase):
    def setUp(self):
        self.request = RequestFactory()

        self.user = User.objects.create(username='test', email='test@gmail.com')
        self.user.set_password('test')

        self.book_one = Book.objects.create(title='blarp', author='wat stick', user=self.user)
        self.book_two = Book.objects.create(title='Gnarf', author='django', user=self.user)

    def test_book_detail_view(self):
        from .views import book_detail_view
        request = self.request.get('')

        request.user = self.user
        
        response = book_detail_view(request, f'{self.book_one.id}')
        self.assertIn(b'wat stick', response.content)

    def test_book_detail_status(self):
        from .views import book_detail_view
        request = self.request.get('')
        request.user = self.user
        response = book_detail_view(request, f'{self.book_one.id}')
        self.assertEqual(200, response.status_code)

    def test_book_detail_date_filter(self):
        from .views import book_detail_view
        request = self.request.get('')
        request.user = self.user
        response = book_detail_view(request, f'{self.book_one.id}')

        self.assertIn(b'Created: Today.', response.content)

