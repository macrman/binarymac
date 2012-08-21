from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import timezone
from posts.models import Post


class TestBlogPageListView(TestCase):

    def test_blog_url_shows_links_to_all_posts(self):
        # setup a post
        post1 = Post(
            title="First Post Title",
            pub_date=timezone.now(),
            content="Content for the first post",
        )
        post1.save()

        # setup another post
        post2 = Post(
            title="Second Post Title",
            pub_date=timezone.now(),
            content="content for the second post",
        )
        post2.save()

        response = self.client.get('/blog')

        # check we used the right template
        self.assertTemplateUsed(response, 'post.html')

        # check we passed the posts to the template

        # check that the post titles appear on page

        # check that the page also has links to the individual post pages
