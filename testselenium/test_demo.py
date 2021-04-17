from selenium import webdriver


class TestEmail:
    def test_email(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("kw").send_keys("测试学院")
