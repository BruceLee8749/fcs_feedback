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

    def test_ZMYF_9507_1(self):
        """参数isShowList，参数为0，文档左右空白部分大小是否统一"""
        if get_cell(fcs_result_path, 18, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 18, 10, sheet_name)
        driver.open_bro(url)
        sleep(2)
        """截图验证"""
        assert driver.screenshot_save(18, sheet_name) == 0
