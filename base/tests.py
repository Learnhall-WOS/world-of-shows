from django.test import TestCase
from .models import Theater, Genre, Talent, Show, Review
from django.contrib.auth.models import User


# Create your tests here.

class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpass')
        self.reviewer = User.objects.create(username='reviewer', password='testpass')
        self.theater = Theater.objects.create(
            name='Test Theater',
            user=self.user
        )
        self.genre = Genre.objects.create(name='Test Genre')
        self.talent = Talent.objects.create(name='Test Talent')
        self.show = Show.objects.create(
            name='Test Show',
            host=self.theater,
            description='Test Description',
        )
        self.show.genre.add(self.genre)
        self.show.talent.add(self.talent)
        self.review = Review.objects.create(
            author=self.reviewer,
            show=self.show,
            text='Test Text'
        )

    def test_theater_model(self):
        self.assertEqual(str(self.theater), 'Test Theater')
        self.assertEqual(self.theater.user, self.user)

    def test_genre_model(self):
        self.assertEqual(str(self.genre), 'Test Genre')

    def test_talent_model(self):
        self.assertEqual(str(self.talent), 'Test Talent')

    def test_show_model(self):
        self.assertEqual(str(self.show), 'Test Show')
        self.assertEqual(self.show.host, self.theater)
        self.assertEqual(self.show.description, 'Test Description')
        self.assertEqual(self.show.genre.first(), self.genre)
        self.assertEqual(self.show.talent.first(), self.talent)

    def test_review_model(self):
        self.assertEqual(str(self.review), 'Test Text')
        self.assertEqual(self.review.text, 'Test Text')
        self.assertEqual(self.review.author, self.reviewer)
        self.assertEqual(self.review.show, self.show)


class TestViews(TestCase):
    def test_login_view(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/login_register.html')

    def test_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/home.html')