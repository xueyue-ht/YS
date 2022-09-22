from selenium import webdriver
from ADJ.utils import times
class Test_Login:
    def test_get_login(self):
        driver=webdriver.Chrome()
        driver.get('https://vue-test.mophone.net/user/login')
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//input[@placeholder='请输入帐户名']").send_keys('13755053575')
        driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys('13755053575')
        cookie_dict={'X-Access-Token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjM4MzYxMTIsInVzZXJuYW1lIjoiMTM3NTUwNTM1NzUifQ.x1quVuXEb3NZQLreh3N1VFZ37XAwAEEYjHBdhPtIyqY'}
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.add_cookie(cookie_dict)
        driver.refresh()
        times.sleep(3)