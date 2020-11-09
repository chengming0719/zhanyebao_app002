from appium import webdriver
import yaml
import logging.config
from os import path

log_file_path = path.join(path.dirname(path.abspath(__file__)), r'D:\pycharm\zhanyebao_app\config\log.conf')
logging.config.fileConfig(log_file_path)
# CON_LOG='../log/log.conf'
# logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()


def appium_desired():
    with open(r'D:\pycharm\zhanyebao_app\config\zhanyebao_caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file)
    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platforVersion'] = data['platforVersion']
    desired_caps['deviceName'] = data['deviceName']

    desired_caps['app'] = data['app']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']

    desired_caps['uicodeKeyboard'] = data['uicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    logging.info('start app...')
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)
    driver.implicitly_wait(8)
    return driver


if __name__ == '__main__':
    appium_desired()