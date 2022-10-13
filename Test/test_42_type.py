import pytest
from main import BrowserAction
from time import sleep
import json
from tools import *

driver = BrowserAction()
pro_path = os.path.dirname(os.path.dirname(__file__))
path = get_conf('FCS', '测试结果文件夹')
fcs_result_path = pro_path + "/" + path
sheet_name = 'Sheet0'


class TestCase:

    def test_convert42_001(self):
        """参数isShowList，参数为0不展示文档目录"""
        if get_cell(fcs_result_path, 10, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 10, 10, sheet_name)
        driver.open_bro(url)
        assert driver.get_attribute("//*[@id='sidebarToggle']",
                                    "style") == 'display: none;'  # 验证该元素的style值为display：none

    def test_convert42_002(self):
        """参数isShowList，参数为1展示文档目录"""
        if get_cell(fcs_result_path, 11, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 11, 10, sheet_name)
        driver.open_bro(url)

        element = driver.find_ele("//*[@id='sidebarToggle']")
        attrs = driver.get_value(element)  # 获取全部的value
        assert "display: none;" not in attrs  # 验证value中不存在display：none
        sleep(2)
        """截图验证"""
        assert driver.screenshot_save(11, sheet_name) == 0

    def test_convert42_003(self):
        """分别在自动缩放、实际大小、适合页面、适合页宽的情况下，多次点击“-”至缩小到10%"""
        if get_cell(fcs_result_path, 20, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 20, 10, sheet_name)
        driver.open_bro(url)
        sleep(1)
        driver.click_zoom_number("自动缩放", 4)  # 下拉菜单中点击自动缩放，再点击5次缩小按钮
        sleep(1)
        element = driver.find_ele("//button[@title='缩小']")
        attrs = driver.get_value(element)
        assert "disabled" in attrs  # 验证value值中存在disable
        sleep(1)
        driver.click_zoom_number("实际大小", 8)  # 下拉菜单中点击实际大小，再点击9次缩小按钮
        sleep(1)
        element = driver.find_ele("//button[@title='缩小']")
        attrs1 = driver.get_value(element)
        assert "disabled" in attrs1
        sleep(1)
        driver.click_zoom_number("适合页面", 1)  # 下拉菜单中点击适合页面，再点击2次缩小按钮
        sleep(1)
        element = driver.find_ele("//button[@title='缩小']")
        attrs2 = driver.get_value(element)
        assert "disabled" in attrs2
        sleep(1)
        driver.click_zoom_number("适合页宽", 4)  # 下拉菜单中点击适合页宽，再点击5次缩小按钮
        sleep(1)
        element = driver.find_ele("//button[@title='缩小']")
        attrs3 = driver.get_value(element)
        assert "disabled" in attrs3
