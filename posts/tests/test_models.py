from django.test import TestCase
from django.utils import timezone
from posts.models import Post


class PostModelTest(TestCase):

    def test_can_create_new_post_and_save_to_db(self):
        # Create a new post object
        post = Post()
        post.title = "Hello World"
        post.pub_date = timezone.now()
        post.content = "Hello everybody, this is a new blog post"

        # check that we can save the post
        post.save()

        # check that there is only 1 post in db
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)

        # check that the only post is the one we just created
        only_post_in_db = all_posts[0]
        self.assertEquals(only_post_in_db, post)

        # check that we saved all the attributes
        self.assertEquals(only_post_in_db.title, post.title)
        self.assertEquals(only_post_in_db.pub_date, post.pub_date)
        self.assertEquals(only_post_in_db.content, post.content)
