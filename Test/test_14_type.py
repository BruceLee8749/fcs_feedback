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

    def test_ZMYF_9311(self):
        """参数isSignature，参数为1，签批后保存，刷新后保存内容正常显示"""
        if get_cell(fcs_result_path, 15, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 15, 10, sheet_name)
        driver.open_bro(url)
        sleep(2)
        driver.click_ele("//img[@title='签批']")  # 点击签批按钮
        sleep(1)
        driver.click_ele("//div[text()='文本']")  # 点击文本
        sleep(1)
        driver.click_ele("//*[@id='content']")  # 点击页面插入文本框
        sleep(1)
        driver.input_sign("签批内容签批内容")  # 签批文本框输入文本
        sleep(1)
        ele = driver.find_ele("//*[@id='content']")
        driver.move_click(ele)  # 移动到签批文本框左侧100单位
        sleep(1)
        driver.click_ele("//div[@class='save']")  # 点击保存
        sleep(10)
        driver.driver.refresh()  # 刷新页面
        sleep(2)
        """截图验证"""
        driver.screenshot_save(15, sheet_name)

    def test_ZMYF_10097(self):
        """参数isSignature，参数为1，签批后保存，刷新后保存内容正常显示"""
        if get_cell(fcs_result_path, 47, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 47, 10, sheet_name)
        driver.open_bro(url)
        sleep(2)
        driver.click_ele("//img[@title='签批']")  # 点击签批按钮
        sleep(1)
        driver.click_ele("//div[text()='文本']")  # 点击文本
        sleep(1)
        driver.click_ele("//*[@id='content']")  # 点击页面插入文本框
        sleep(1)
        driver.input_sign("签批内容签批内容")  # 签批文本框输入文本
        driver.click_ele("//div[@class='save']")  # 点击保存
        sleep(10)
        driver.driver.refresh()  # 刷新页面
        sleep(2)
        """截图验证"""
        driver.screenshot_save(47, sheet_name)

    def test_ZMYF_10127(self):
        assert get_cell(fcs_result_path, 49, 9, sheet_name) == '通过'

    def test_ZMYF_10154(self):
        if get_cell(fcs_result_path, 50, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 50, 10, sheet_name)
        driver.open_bro(url)
        sleep(2)
        driver.ele_not_exist("//div[@id='page-2']")
