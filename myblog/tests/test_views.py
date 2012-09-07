from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import timezone
from myblog.models import Post, Tag
from myblog.views import PostDetailView
from django.template.defaultfilters import slugify


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

        response = self.client.get('/blog/')

        # check we used the right template
        self.assertTemplateUsed(response, 'post_list.html')

        # check we passed the posts to the template

        # check that the post titles appear on page
        self.assertIn(post1.title, response.content)
        self.assertIn(post2.title, response.content)



        # This will be deprecated with the usage of sluggy urls. YAY!!!
#        # check that the page also has links to the individual post pages
#        post1_url = reverse('post_detail', args=[post1.pk, ])
#        self.assertIn(post1_url, response.content)
#
#        post2_url = reverse('post_detail', args=[post2.pk, ])
#        self.assertIn(post2_url, response.content)


class TestBlogDetailView(TestCase):

    def test_post_url_slug(self):
        # setup a post first
        post = Post()
        post.title = 'demo'
        post.content = 'hello, testing slugs work'
        post.pub_date = timezone.now()
        post.save()

        # check that the slug == a title that has been slugified
        self.assertEquals(post.slug, slugify(post.title))


        # I should probably consider using pks or dates as well
        # along with sluggy urls

        # home/pk/slug
        # home/yyyy/mm/dd/slug
        # home/yyyy/mm/dd/pk/slug

        # check that the slug field is "sluggy"
        sluggy_url = reverse('post_detail', args=[post.pk, post.slug])
        response = self.client.get(sluggy_url)
        # check that the url goes to the post
#        self.assertIn(
