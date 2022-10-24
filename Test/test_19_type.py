import pytest
from selenium.webdriver import Keys

from main import BrowserAction
from time import sleep
import json
from tools import *

driver = BrowserAction()
pro_path = os.path.dirname(os.path.dirname(__file__))
path = get_conf('FCS', '测试结果文件夹')
fcs_result_path = pro_path + "/" + path
sheet_name = '功能参数'


class TestCase:

    def test_ZMYF_10058(self):
        if get_cell(fcs_result_path, 35, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 35, 10, sheet_name)
        print(url)
        driver.open_bro(url)
        driver.click_ele("//span[@class='fcon ico_file_dir']")
        sleep(2)
        driver.click_ele("//span[@class='fcon ico_file_dir']")
        driver.click_ele("//span[contains(text(),'.doc')]")
        sleep(1)
        driver.driver.switch_to.frame(driver.find_ele("//iframe[@class='pica-player pica-frame scroll']"))
        driver.element_input("//input[@id='currentPage']", 41, clear=2)
        driver.screenshot_save(35, sheet_name)