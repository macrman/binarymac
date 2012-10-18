from django.test import TestCase
from tutorials.models import Tutorial, Series

class TutorialModelTest(TestCase):

    def test_can_create_object_and_save_to_db(self):
        hello_tutorial = Tutorial
        hello_tutorial.title = "hello world tutorial"
        #to be continued
