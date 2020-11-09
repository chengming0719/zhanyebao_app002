# coding = utf-8
import unittest
from BSTestRunner import BSTestRunner
import time
import sys

path = 'D:\\pycharm\\zhanyebao_app\\'
sys.path.append(path)
test_dir = '../test_case'
report_dir = '../reports'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_login.py')   # pattern是匹配的测试模块

now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir + '/' + now + ' test_report.html'

with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title='易生展业宝测试报告', description='测试登录功能')
    runner.run(discover)