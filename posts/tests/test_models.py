from django.test import TestCase
from django.utils import timezone
from posts.models import Post


class PostModelTest(TestCase):

    def test_can_create_new_post_and_save_to_db(self):
        # Create a new post object
        post = Post(
            title = "Hello World",
            pub_date = timezone.now(),
            content = "Hello everybody, this is a new blog post",
        )

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

    def test_verbose_name_for_pub_date(self):
        for field in Post._meta.fields:
            if field.name == 'pub_date':
                self.assertEquals(field.verbose_name, "Date published")

    def test_post_objects_are_named_after_title(self):
        p = Post()
        p.title = "This is a blog post"
        self.assertEquals(unicode(p), "This is a blog post")
