from baseView.baseView import BaseView
from common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging, time, csv
from selenium.webdriver.common.by import By
from os import path

class Common(BaseView):
    cancelBtn=(By.ID,'android:id/button2')
    skipBtn=(By.ID,'com.tal.kaoyan:id/tv_skip')
    wemedia_cacel=(By.ID,'com.tal.kaoyan:id/view_wemedia_cacel')

    def check_cancelBtn(self):
        logging.info('===========check cancelBtn==========')
        try:
            cancelBtn=self.driver.find_element(*self.cancelBtn)
        except NoSuchElementException:
            logging.info('no checkBtn')
        else:
            cancelBtn.click()

    def check_skipBtn(self):
        logging.info('============check skipBtn==========')
        try:
            skipBtn=self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('no skipBtn')
        else:
            skipBtn.click()

    def get_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipeLeft(self):
        l = self.get_size()
        x1 = int(l[0]*0.5)
        y1 = int(l[1]*0.5)
        x2 = int(l[0]*0.1)
        self.swipe(x1, y1, x2, y1, 1000)

    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self, module):
        time = self.getTime()
        image_file = path.dirname(path.dirname(__file__)) + '/screenshots/%s_%s.png' %(module,time)

        logging.info('get %s screenshot' %module)
        self.driver.get_screenshot_as_file(image_file)

    # 判断是否有广告弹框
    def check_market_ad(self):
        logging.info('=====check_market_ad=====')
        try:
            element=self.driver.find_element(*self.wemedia_cacel)
        except NoSuchElementException:
            pass
        else:
            logging.info('=====click_wemedia_cancel=====')
            element.click()

    def get_csv_data(self, csv_file, line):
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row


if __name__ == '__main__':
    driver = appium_desired()
    com = Common(driver)
#     com.check_cancelBtn()
#     # com.check_skipBtn()
#     com.swipeLeft()
#     com.getScreenShot('start_APP')

    csv_file = '../data/account.csv'

    data = com.get_csv_data(csv_file, 1)
    print(data)
