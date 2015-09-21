from unittest import TestCase, main
from selenium.webdriver import Chrome


class NewVisitorTest(TestCase):
  def setUp(self):
    self.browser = Chrome()
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()

  def test_home_page(self):
    self.browser.get('localhost:8000')
    self.assertIn('Bulletin', self.browser.title)


if __name__ == '__main__':
  main(warnings='ignore')
