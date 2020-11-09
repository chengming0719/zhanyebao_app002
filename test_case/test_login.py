from bussinessView.loginView import LoginView
from common.myunit import StartEnd
import logging
import unittest


class TestLogin(StartEnd):
    csv_file = '../data/account.csv'

    # @unittest.skip('skip test_login_zxw2017')
    def test_login_zxw2017(self):
        logging.info('========login zxw2017========')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 1)
        l.login_action(data[0], data[1])
        self.assertTrue(l.check_login_status(), msg='login success!')

    # @unittest.skip('skip test_login_zxw2018')
    def test_login_zxw2018(self):
        logging.info('========login zxw2018========')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 2)
        l.login_action(data[0], data[1])
        self.assertTrue(l.check_login_status())

    # @unittest.skip('skip test_login_error')
    def test_login_error(self):
        logging.info('========login error========')
        l = LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 3)
        l.login_action(data[0], data[1])
        self.assertTrue(l.check_login_status(), msg='login fail!')


if __name__ == '__main__':
    unittest.main()