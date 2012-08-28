from django.test import TestCase
from django.utils import timezone
from myblog.models import Post, Tag


class PostModelTest(TestCase):

    def test_can_create_new_post_and_save_to_db(self):
        # Create a new post object
        post = Post(
            title="Hello World",
            pub_date=timezone.now(),
            content="Hello everybody, this is a new blog post",
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


class TagModelTest(TestCase):

    def test_create_tags_for_posts(self):
        # tests posts, postodd will have odd tags, posteven will have even ones
        postodd = Post(
            title="testing odd tags",
            pub_date=timezone.now(),
            content='''hello everybody, we are testing some tagging
                functionality here. This post should have odd tags.''',
        )
        posteven = Post(
            title="test even tags",
            pub_date=timezone.now(),
            content ='''hello everybody, we are testing some tagging
                functionality here. This post should have even tags.''',
        )
        #save them to db
        postodd.save()
        posteven.save()

        # create the  tags
        tag1 = Tag(name="1")
        tag2 = Tag(name="2")
        tag3 = Tag(name="3")
        tag4 = Tag(name="4")

        # save all tags to db
        tag1.save()
        tag2.save()
        tag3.save()
        tag4.save()

        # create the many2many relationship
        postodd.tag.add(tag1)

        # check that the posteven and postodd both have 2 tags
        # check that the odd posts have the tags 1 and 3
        # check that the even posts have the tags 2 and 4
