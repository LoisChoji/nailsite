from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from .models import Allpolishes

class AllpolishesModelTest(TestCase):
    def test_was_pubished_recently_with_future_course(self):
        time = timezone.now() + datetime.timedelta(days = 30)
        future_question = Allpolishes(startedfrom = time)
        self.assertIs(future_question.was_published_recently(), False)
    
    def test_was_published_recently_with_old_course(self):
        test = timezone.now() - datetime.timedelta(days = 1, seconds = 1)
        old_polish=  Allpolishes(startedfrom = time)
        self.assertIs((old_polish.was_published_recently(), False))

    def test_was_published_recently_with_recent_course(self):
        test = timezone.now() - datetime.timedelta(hours = 23, minutes = 59, seconds = 59)
        old_polish=  Allpolishes(startedfrom = time)
        self.assertIs((old_polish.was_published_recently(), True))

    