import unittest
# import sys
# sys.path.append('./')
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from ddt import ddt,data,unpack
from common.create_driver import getDriver
from common.manage_dir import getFileName
from common.file_operation import *
import time

@ddt
class UserActionTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = getDriver()
        cls.driver.implicitly_wait(20)
        

    def setUp(self):
        self.driver.get('http://118.31.19.120:3000/signin')
        time.sleep(1)


    def login(self,username, passwd):
        # self.driver.find_element_by_link_text('登录').click()
        self.driver.find_element_by_id('name').send_keys(username)
        self.driver.find_element_by_id('pass').send_keys(passwd)
        self.driver.find_element_by_id('pass').submit()
        
        url = self.driver.current_url
        return self.assertEquals(url,'http://118.31.19.120:3000/')


    def post(self,title, content):
        self.driver.find_element_by_css_selector('.span-success').click()
        self.driver.find_element_by_css_selector('#tab-value').click()
        self.driver.find_element_by_xpath('//*[@id="tab-value"]/option[3]').click()
        self.driver.find_element_by_id('title').send_keys(title)
        self.driver.find_element_by_css_selector('.CodeMirror-scroll').click()
        #for windows
        # ActionChains(driver).send_keys(Keys.COMMAND + 'b').send_keys(content).perform()
        # for mac
        ActionChains(self.driver).key_down(Keys.COMMAND).send_keys('b').key_up(Keys.COMMAND).send_keys(content).perform()
        self.driver.find_element_by_css_selector('.span-primary.submit_btn').click()


    def delpost(self):
        wnds = self.driver.window_handles
        self.driver.switch_to_window(wnds[-1])
        self.driver.find_element_by_xpath('//*[@id="manage_topic"]/a[2]/i').click()
        self.driver.switch_to_alert().accept()

    # def test_register(self):
    #     self.driver.find_element_by_link_text('注册').click()
    #     self.driver.find_element_by_id('loginname').send_keys('user25')
    #     self.driver.find_element_by_id('pass').send_keys('123456')
    #     self.driver.find_element_by_id('re_pass').send_keys('123456')
    #     self.driver.find_element_by_id('email').send_keys('82873909@125.com')
    #     self.driver.find_element_by_css_selector('.span-primary').click()

    #     info = self.driver.find_element_by_css_selector('.alert.alert-success').text
    #     self.assertEqual(info,'欢迎加入 Nodeclub！我们已给您的注册邮箱发送了一封邮件，请点击里面的链接来激活您的帐号。')


    @data(*get_data('testdata/userinfo.csv'))
    @unpack
    def test_flow(self,username,passwd,title,content):
        if(self.login(username,passwd)!= 'FAIL'):
            self.post(title,content)
        else:
            print('log failed')

    def tearDown(self):
        self.driver.save_screenshot(getFileName('screenshots','png'))
        self.driver.delete_all_cookies()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

        
    
