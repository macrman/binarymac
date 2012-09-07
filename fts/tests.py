from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SiteTest(LiveServerTestCase):
    fixtures = ['admin_user.json']

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
    
    def _admin_login(self):
        # admin goes to admin site
        self.browser.get(self.live_server_url + '/admin/')

        # sees form to login
        username_field = self.browser.find_element_by_name('username')
        password_field = self.browser.find_element_by_name('password')

        # enters her credentials
        username_field.send_keys('admin')
        password_field.send_keys('adm1n')
        password_field.send_keys(Keys.RETURN)
        

    def _setup_blog_post_without_tags(self):
        '''Creates a post without a tag, testing the that tags are option,
        and that prepopulating slugs work. Requires _admin_login.'''

        # she sees the link for posts and clicks it
        posts_link = self.browser.find_element_by_link_text('Posts')
        posts_link.click()

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

        # she sees that the slug has already been prepopulated

        # she hit's save, and now it's published
        save_button = self.browser.find_element_by_css_selector(
            "input[value='Save']"
        )
        save_button.click()

        # She goes back to the root of the admin site
        self.browser.get(self.live_server_url + '/admin/')

        # She logs out of the admin site
        self.browser.find_element_by_link_text('Log out').click()

    def test_can_view_blog_post(self):
        # Karen logs into admin, creates a blog post, logs out.
        self._admin_login()
        self._setup_blog_post_without_tags()

        # Jim goes to the the home page
        self.browser.get(self.live_server_url)

        # Jim sees a link to a blog, so he clicks it
        blog_link = self.browser.find_element_by_link_text('Blog')
        blog_link.click()

        # He sees a list of blog posts
        # clicks on the first one
        first_post_link = 'My Very First Blog Post'
        self.browser.find_element_by_link_text(first_post_link).click()

        self.fail("Weeeee! Yay for self fail!!!!!")
