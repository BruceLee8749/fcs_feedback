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
        if get_cell(fcs_result_path, 9, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 9, 10, sheet_name)
        driver.open_bro(url)
        sleep(2)
        assert driver.get_attribute("//*[@id='sidebarToggle']",
                                    "style") == 'display: none;'  # 验证该元素的style值为display：none

    def test_convert42_002(self):
        """参数isShowList，参数为1展示文档目录"""
        if get_cell(fcs_result_path, 10, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 10, 10, sheet_name)
        driver.open_bro(url)
        element = driver.find_ele("//*[@id='sidebarToggle']")
        attrs = driver.get_value(element)  # 获取全部的value
        assert "display: none;" not in attrs  # 验证value中不存在display：none
        sleep(2)
        """截图验证"""
        assert driver.screenshot_save(10, sheet_name) == 0

    def test_convert42_003(self):
        """参数isShowList，参数为0，文档左右空白部分大小是否统一"""
        if get_cell(fcs_result_path, 19, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 19, 10, sheet_name)
        driver.open_bro(url)
        sleep(2)
        """截图验证"""
        assert driver.screenshot_save(19, sheet_name) == 0

    def test_convert42_004(self):
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

    def test_convert42_005(self):
        """参数isFullScreen，参数为0不展示全屏按钮"""
        if get_cell(fcs_result_path, 24, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 24, 10, sheet_name)
        driver.open_bro(url)
        sleep(1)
        assert driver.get_attribute("//*[@id='presentationMode']",
                                    "style") == 'display: none;'  # 验证该元素的style值为display：none
        """截图验证"""
        assert driver.screenshot_save(24, sheet_name) == 0

    def test_convert42_006(self):
        """参数isPrint，参数为1转换和打开文档正常"""
        if get_cell(fcs_result_path, 25, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 25, 10, sheet_name)
        driver.open_bro(url)
        sleep(2)
        """截图验证"""
        assert driver.screenshot_save(25, sheet_name) == 0

    def test_convert42_007(self):
        """参数isShowList，参数为1目录中最后一个目录下方无其他无关内容显示"""
        if get_cell(fcs_result_path, 34, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 34, 10, sheet_name)
        driver.open_bro(url)
        sleep(2)
        driver.swap_scroll("//a[contains(text(),'保全变更')]")  # 滑动滚动条到对应最后一个元素位置
        sleep(2)
        """截图验证"""
        assert driver.screenshot_save(34, sheet_name) == 0
