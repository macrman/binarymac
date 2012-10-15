from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils import timezone
from myblog.models import Post, Tag
from myblog.views import PostDetailView
from django.template.defaultfilters import slugify


class TestBlogPageListView(TestCase):

    def test_blog_url_shows_links_to_posts(self):
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
        self.assertTemplateUsed(response, 'blog.html')

        # check we passed the posts to the template

        # check that the post titles appear on page
        self.assertIn(post1.title, response.content)
        self.assertIn(post2.title, response.content)

        # test pagination


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
        self.assertIn('testing', response.content)


class TestPostListByTag(TestCase):

    def test_page_shows_post_by_tag(self):
        post1 = Post()
        post1.title = 'hello'
        post1.content = "hi"
        post1.pub_date = timezone.now()
        post1.save()
        
        post2 = Post()
        post2.title = "world"
        post2.content = "earth"
        post2.pub_date = timezone.now()
        post2.save()

        # create a tag
        hellotag = Tag()
        hellotag.name = 'hello'
        hellotag.save()
        
        worldtag = Tag()
        worldtag.name = 'world'
        worldtag.save()

        # create the relationship between tag and post
        post1.tag.add(hellotag)
        post2.tag.add(worldtag)

        # go to the page that only shows posts that are tagged "hello"
        posts_tagged_as_hello_response = reverse('tagged_post_list', args=[hellotag.name])
        # check that post1 is on that page
        self.assertIn(post1.title, posts_tagged_as_hello_response)
        # check that post2 is not on the page
        self.assertNotIn(post2.title, posts_tagged_as_hello_response)
        # go to the page that shows posts which are tagged "world"
        posts_tagged_as_world_response = reverse('tagged_post_list', args=[worldtag.name])
        # check that post2 is shows up on that page
        self.assertIn(post2.title, posts_tagged_as_world_response)
        # check that post1 is not on the page
        self.assertNotIn(post1.title, posts_tagged_as_world_response)


