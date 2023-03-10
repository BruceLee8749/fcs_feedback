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

    def test_ZMYF_8888_2(self):
        """ZMYF-8888参数isDccAsync"""
        if get_cell(fcs_result_path, 8, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 8, 10, sheet_name)
        print(url)
        driver.open_bro(url)
        driver.element_input("//input[@id='currentPage']", 9, clear=2)
        # driver.screenshot_save(8, sheet_name)
        driver.screenshot_save(8, sheet_name)

    def test_ZMYF_9575(self):
        """ZMYF-9575验证转换类型61下是否有播放按钮"""
        if get_cell(fcs_result_path, 21, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 21, 10, sheet_name)
        print(url)
        driver.open_bro(url)
        driver.ele_exist("//img[@title='播放']")  # 验证有“播放”按钮存在

    def test_ZMYF_10050(self):
        """ZMYF-10050参数isShowList，参数为1展示文档目录"""
        if get_cell(fcs_result_path, 25, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 25, 10, sheet_name)
        driver.open_bro(url)
        driver.ele_exist("//img[@title='目录']")  # 验证参数为1时，有“目录”按钮存在
        driver.click_ele("//img[@title='目录']")  # 点击“目录”按钮
        sleep(5)
        """截图验证"""
        driver.screenshot_save(25, sheet_name)

    def test_ZMYF_9491(self):
        """ZMYF-9491参数isShowList，参数为1展示文档目录"""
        if get_cell(fcs_result_path, 31, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 31, 10, sheet_name)
        driver.open_bro(url)
        driver.ele_exist("//img[@title='目录']")  # 验证参数为1时，有“目录”按钮存在
        driver.click_ele("//img[@title='目录']")  # 点击“目录”按钮
        sleep(5)
        """截图验证"""
        driver.screenshot_save(32, sheet_name)

    def test_ZMYF_10112(self):
        assert get_cell(fcs_result_path, 48, 9, sheet_name) == '通过'

    def test_ZMYF_8699(self):
        assert get_cell(fcs_result_path, 58, 9, sheet_name) == '通过'

    def test_ZMYF_8699_1(self):
        assert get_cell(fcs_result_path, 59, 9, sheet_name) == '通过'

    def test_ZMYF_8751_2(self):
        assert get_cell(fcs_result_path, 61, 9, sheet_name) == '通过'

    def test_ZMYF_9171(self):
        assert get_cell(fcs_result_path, 62, 9, sheet_name) == '通过'

    def test_ZMYF_9262_3(self):
        assert get_cell(fcs_result_path, 67, 9, sheet_name) == '通过'
