import logging
from common.common_fun import Common
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


class LoginView(Common):

    # 考研帮app元素
    # username_type = (By.ID,'com.tal.kaoyan:id/login_email_edittext')
    # password_type = (By.XPATH,'//*[@class="android.widget.EditText" and @index="3"]')
    # log_btn = (By.ID,'com.tal.kaoyan:id/login_login_btn')
    #
    # tip_commit = (By.ID,'com.tal.kaoyan:id/tip_commit')
    #
    # button_mysefl = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')
    # usercenter_username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')
    #
    # RightButton = (By.ID, 'com.tal.kaoyan:id/myapptitle_RightButton_textview')
    # button_logout = (By.ID, 'com.tal.kaoyan:id/setting_logout_text')

    #易生展业宝app元素
    username_type = (By.XPATH, '//android.view.View[@content-desc="pages/index/index[2]"]/android.widget.EditText[1]')
    password_type = (By.XPATH, '//android.view.View[@content-desc="pages/index/index[2]"]/android.widget.EditText[2]')
    log_btn = (By.XPATH, '//android.view.View[@content-desc="登录"]')
    mer_account = (By.XPATH, '//android.view.View[@content-desc="商户入网"]')

    def login_action(self, username, password):
        self.check_cancelBtn()
        self.check_skipBtn()

        logging.info("==========login action==========")
        user = self.driver.find_element(*self.username_type)
        pwd = self.driver.find_element(*self.password_type)

        logging.info('username is: %s'%username)
        user.send_keys(username)
        logging.info('password is: %s'%password)
        time.sleep(1)
        pwd.send_keys(password)

        logging.info('==========click log_btn==========')
        self.driver.find_element(*self.log_btn).click()
        time.sleep(1)
        logging.info('===========login finish==========')

    # 判断用户是否登录成功
    def check_account_alert(self):
        logging.info('==========check_account_alert==========')
        try:
            element = self.driver.find_element(*self.mer_account)
        except NoSuchElementException:
            pass
        else:
            logging.info('close tip_commit')
            element.click()

    def check_login_status(self):
        logging.info('==========check_login_status===========')

        self.check_market_ad()
        self.check_account_alert()

        try:
            element = self.driver.find_element(*self.mer_account)
        except NoSuchElementException:
            logging.info('login fail')
            self.getScreenShot('login_fail')
            pass
            return False
        else:
            return True

        # try:
        #     #展业宝
        #     self.driver.find_element(*self.mer_account).click()
        #
        #     #考研帮app
        #     # self.driver.find_element(*self.button_mysefl).click()
        #     # self.find_element(*self.usercenter_username)
        # except NoSuchElementException:
        #     logging.info('login fail')
        #     self.getScreenShot('login_fail')
        #     return False
        # else:
        #     logging.info('login success')
        #     self.logout_action()
        #     return True

    def logout_action(self):
        logging.info('==========logout==========')
        self.driver.find_element(*self.RightButton).click()
        self.driver.find_element(*self.button_logout).click()
        self.driver.find_element(*self.tip_commit).click()


if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    # l.login_action("2018", "zxw2018")
    l.check_login_status()

