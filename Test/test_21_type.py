import pytest
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

    def test_ZMYF_8743(self):
        """ZMYF-8743验证转换类型21下菜单栏是否会缩回"""
        if get_cell(fcs_result_path, 3, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 3, 10, sheet_name)
        driver.open_bro(url)
        driver.click_ele("//button[@title='文档管理']")
        driver.click_ele("//button[@title='文档管理']")
        sleep(2)
        assert driver.get_attribute("//button[@title='文档管理']", "style") != "background-color: rgb(235, 232, 232);"

    def test_ZMYF_9239(self):
        """ZMYF-9329验证转换类型21下打印"""
        if get_cell(fcs_result_path, 11, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 11, 10, sheet_name)
        driver.open_bro(url)
        driver.click_ele("//input[@type='checkbox']")
        sleep(1)
        driver.click_ele("//*[text()=' 全选 ']")
        sleep(1)
        driver.click_ele("//*[text()='文件 ']")
        sleep(1)
        driver.click_ele("//*[text()=' 打印 ']")
        sleep(1)
        driver.screenshot_save(11, sheet_name)
