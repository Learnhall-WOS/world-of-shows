from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import Play
from datetime import datetime, timezone
import uuid

class PlayModelTestCase(TestCase):
    def test_create_play_with_uuid(self):
        # generate a UUID for the play_id field
        play_id = uuid.uuid4()

        # create a new Play object
        play = Play.objects.create(
            play_id=play_id,
            name='Hamlet',
            author='William Shakespeare',
            genre='Tragedy',
            description='The play follows Prince Hamlet as he seeks revenge on his uncle for murdering his father.'
        )

        # verify that the play was created with the correct data
        self.assertEqual(play.play_id, play_id)
        self.assertEqual(play.name, 'Hamlet')
        self.assertEqual(play.author, 'William Shakespeare')
        self.assertEqual(play.genre, 'Tragedy')
        self.assertEqual(play.description, 'The play follows Prince Hamlet as he seeks revenge on his uncle for murdering his father.')

class PlaySearchTestCase(TestCase):
    def setUp(self):
        # create test plays
        Play.objects.create(
            name='Hamlet',
            author='William Shakespeare',
            genre='Tragedy',
            description='The play follows the life of Prince Hamlet as he tries to avenge his father’s death.'
        )
        Play.objects.create(
            name='Romeo and Juliet',
            author='William Shakespeare',
            genre='Tragedy',
            description='The play tells the story of two young lovers whose deaths ultimately reconcile their feuding families.'
        )
        Play.objects.create(
            name='A Midsummer Night’s Dream',
            author='William Shakespeare',
            genre='Comedy',
            description='The play portrays the events surrounding the marriage of Theseus, the Duke of Athens, to Hippolyta.'
        )
        Play.objects.create(
            name='The Importance of Being Earnest',
            author='Oscar Wilde',
            genre='Comedy',
            description='The play is a satire on Victorian society, and focuses on the courtship of two young ladies and their respective beaus.'
        )
        
    def test_home_play_reads_view(self):
        # create a test client and fetch the Home Play Reads page
        response = self.client.get(reverse('home_play_reads'))

        # verify that the response status code is 200
        self.assertEqual(response.status_code, 200)
        
        # verify site still on home_play_reads
        self.assertTemplateUsed(response, 'playreads/home_play_reads.html')
        
        # verify that all three Play objects are displayed on the page
        self.assertContains(response, 'Hamlet')
        self.assertContains(response, 'Romeo and Juliet')
        self.assertContains(response, 'A Midsummer Night’s Dream')
        self.assertContains(response, 'The Importance of Being Earnest')
        
        
    def test_search_by_name(self):
        response = self.client.get(reverse('home_play_reads'), {'q': 'Hamlet'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'playreads/home_play_reads.html')
        self.assertContains(response, 'Hamlet')
        self.assertNotContains(response, 'Romeo and Juliet')
        self.assertNotContains(response, 'A Midsummer Night’s Dream')
        self.assertNotContains(response, 'The Importance of Being Earnest')

    def test_search_by_author(self):
        response = self.client.get(reverse('home_play_reads'), {'q': 'William Shakespeare'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'playreads/home_play_reads.html')
        self.assertContains(response, 'Hamlet')
        self.assertContains(response, 'Romeo and Juliet')
        self.assertContains(response, 'A Midsummer Night’s Dream')
        self.assertNotContains(response, 'The Importance of Being Earnest')

    def test_search_by_genre(self):
        response = self.client.get(reverse('home_play_reads'), {'q': 'Comedy'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'playreads/home_play_reads.html')
        self.assertNotContains(response, 'Hamlet')
        self.assertNotContains(response, 'Romeo and Juliet')
        self.assertContains(response, 'A Midsummer Night’s Dream')
        self.assertContains(response, 'The Importance of Being Earnest')
        
class ParticipateViewTestCase(TestCase):
    def setUp(self):
        # self.client = Client()
        self.play = Play.objects.create(name='Test Play', author='Test Author', genre='Test Genre')

    def test_participate_form_submission(self):
        url = reverse('participate', args=[str(self.play.play_id)])
        response = self.client.post(url, {'name': 'John Doe', 'email': 'john@example.com'})

        self.assertEqual(response.status_code, 302) # Should redirect to play detail page
        self.assertRedirects(response, reverse('play_detail', args=[str(self.play.play_id)]))
        self.assertEqual(len(get_messages(response.wsgi_request)), 1) # Success message displayed

    def test_participate_invalid_form_submission(self):
        url = reverse('participate', args=[str(self.play.play_id)])
        response = self.client.post(url, {'name': '', 'email': ''})

        self.assertEqual(response.status_code, 302) # Should redirect to play detail page
        self.assertRedirects(response, reverse('play_detail', args=[str(self.play.play_id)]))
        self.assertEqual(len(get_messages(response.wsgi_request)), 1) # Error message displayed