from django.test import TestCase
from simplepages.models import Page


class PageModelTest(TestCase):

    def test_create_page_object(self):
        # create a Page object
        samplepage = Page()
        samplepage.title = "hello, this is my first page"
        samplepage.content = "Here is some random content. Good bye"

        # check we can save it
        samplepage.save()

        # check there is only 1 Page object in db
        all_pages = Page.objects.all()
        self.assertEquals(len(all_pages), 1)

        # check that the only object in db is the one we created
        only_page = all_pages[0]
        self.assertEquals(only_page, samplepage)

        # check that all the attibutes are saved as well
        self.assertEquals(only_page.title, samplepage.title)
        self.assertEquals(only_page.content, samplepage.content)

    def test_slug_is_named_after_title(self):
        # create Page object
        p = Page(title="hi there", content="wee")
        p.save()

        # checks slug is named after title and is properly "slugified"
        self.assertEquals(p.slug, "hi-there")

    def test_page_objects_are_names_after_its_title(self):
        p = Page()
        p.title = "hello world"
        p.content = "blah blah blah"
        p.save()
        self.assertEquals(unicode(p), "hello world")
