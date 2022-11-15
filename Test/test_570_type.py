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

    def test_ZMYF_10194(self):
        assert get_cell(fcs_result_path, 51, 9, sheet_name) == '通过'