import self
from selenium import webdriver

def setUp(self):
    # Initialize webdriver
    self.driver = webdriver.Chrome(r"C:\Users\Wasim.Sajjad\Downloads\chromedriver_win32\chromedriver.exe")


def teardown(self):
    self.driver.close()


def test_login(self):
    self.driver.get('https://www.hotmail.com')
    self.driver.implicitly_wait(self.driver.title == 'Outlook – free personal email and calendar from Microsoft')
    signInbtn=self.driver.find_element_by_css_selector('body > header > div > aside > div > nav > ul > li:nth-child(2) > a')
    signInbtn.click()
    self.driver.implicitly_wait(self.driver.find_element_by_class_name('logo').is_displayed())
    emailfield=self.driver.find_element_by_id('i0116')
    emailfield.send_keys('wasim.sajjad1214@hotmail.com')
    nextbtn=self.driver.find_element_by_id('idSIButton9')
    nextbtn.click()

    # self.driver.implicitly_wait(self.driver.find_element_by_css_selector('##displayName').is_displayed())
    # self.assertIn("wasim", self.driver.find_element_by_title ('wasim.sajjad1214@hotmail.com'))
    passwordfield=self.driver.find_element_by_xpath('//*[@id="i0118"]')
    passwordfield.send_keys('NullNull')
    loginbtn = self.driver.find_element_by_css_selector('#idSIButton9[value="Sign in"]')
    loginbtn.click()
    # self.assertIn("incorrect", self.driver.find_element_by_id('passwordError'))

setUp(self)
test_login(self)
teardown(self)



