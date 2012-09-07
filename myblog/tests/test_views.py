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


class TestBlogDetailView(TestCase):

    def test_post_url_slug(self):
        # setup a post first
        post = Post()
        post.title = 'demo'
        post.content = 'hello, testing slugs work'
        post.pub_date = timezone.now()
        post.save()
        
        # create a tag 
        tag = Tag()
        tag.name = 'testing'
        tag.save()

        # add the tag to post
        post.tag.add(tag)

        # check that the slug == a title that has been slugified
        self.assertEquals(post.slug, slugify(post.title))

        # check that the slug field is "sluggy"
        sluggy_url = reverse('post_detail', args=[post.pk, post.slug])
        response = self.client.get(sluggy_url)

        # test that all the objects have been pasted to the template
        self.assertIn(post.title, response.content)
        self.assertIn(post.content, response.content)
        # todo:
        # self.assertIn(str(post.pub_date), response.content)
        self.assertIn('testing', response.content)
