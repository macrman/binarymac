from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SiteTest(LiveServerTestCase):
    fixtures = ['admin_user.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_can_create_blog_post(self):
        # admin wants to create a post, goes to admin site
        self.browser.get(self.live_server_url + '/admin/')

        # she sees the django login page
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        # she sees the form to login
        username_field = self.browser.find_element_by_name('username')
        password_field = self.browser.find_element_by_name('password')

        # she enters her credentials and hits return
        username_field.send_keys('admin')
        password_field.send_keys('adm1n')
        password_field.send_keys(Keys.RETURN)

        # she sees 2 links for posts
        posts_links = self.browser.find_elements_by_link_text('Posts')
        self.assertEquals(len(posts_links), 2)


        # she clicks on the 2nd one
        posts_links[1].click()

        # she sees that she hasn't written any blog posts yet!
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('0 posts', body.text)

        # she decides to make a new post
        new_post = self.browser.find_element_by_link_text('Add post')
        new_post.click()

        # she sees the input form to make a new post
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Title', body.text)
        self.assertIn('Date published', body.text)

        # she fills out the title of her post
        title_field = self.browser.find_element_by_name('title')
        title_field.send_keys('My Very First Blog Post')

        # she feels lazy so she justs clicks 'today' and 'now' for the date
        today_link = self.browser.find_element_by_link_text('Today')
        today_link.click()
        now_link = self.browser.find_element_by_link_text('Now')
        now_link.click()

        # she writes out her blog post
        content_field = self.browser.find_element_by_name('content')
        content_field.send_keys(
            "Hello Everyone, this is my first blog post. I hope you enjoy it"
        )
        # she hit's save, and now it's published
        save_button = self.browser.find_element_by_css_selector(
            "input[value='Save']"
        )
        save_button.click()

    def NOTtest_can_create_new_poll_via_admin_site(self):

        # She types in her username and passwords and hits return
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('adm1n')
        password_field.send_keys(Keys.RETURN)





    def NOTtest_can_post_comment_on_blog(self):
        # Jim goes to the the home page
        self.browser.get(self.live_server_url)

        # Jim sees a link to a blog, so he clicks it
        blog_link = self.browser.find_element_by_link_text('Blog')
        blog_link.click()

        # He sees a list of blog posts, clicks on the first one
        blog_post_link = self.browser.find_element_by_class()

        self.fail("Weeeee! Yay for self fail!!!!!")
