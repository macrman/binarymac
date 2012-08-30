from django.test import TestCase
from simplepages.models import Page
from django.core.urlresolvers import reverse


class SinglePageViewTest(TestCase):

    def test_slug_url_goes_to_detail_view(self):
        # setup Page
        page1 = Page(title="hola", content="amigo")
        page2 = Page(title="hello there", content="world")

        page1.save()
        page2.save()

        #this also tests sluggy urls

        page2_url = reverse('page_detail', args=[page2.slug, ])
        response = self.client.get(page2_url)

        # check correct template was used
        self.assertTemplateUsed(response, 'page_detail.html')

        # check we've passed the correct object to the template
        self.assertEquals(response.context['page'], page2)

        # check the title and content appears on page
        self.assertIn(page2.title, response.content)
        self.assertIn(page2.content, response.content)
