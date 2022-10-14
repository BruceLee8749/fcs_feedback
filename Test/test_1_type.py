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

    def test_2512(self):
        """参数isHeaderBar为0，不显示头部导航栏"""
        if get_cell(fcs_result_path, 29, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 29, 10, sheet_name)
        driver.open_bro(url)
        driver.ele_not_exist("//div[@class='container-fluid']")  # 验证头部导航栏这个元素不存在
