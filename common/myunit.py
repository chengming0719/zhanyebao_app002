import unittest
from common.desired_caps import appium_desired
import logging
import time


class StartEnd(unittest.TestCase):

    def setUp(self):
        logging.info('==========set up==========')
        self.driver=appium_desired()

    def tearDown(self):
        logging.info('==========tear down==========')
        time.sleep(5)
        self.driver.close_app()