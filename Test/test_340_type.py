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

    def test_ZMYF_8846(self):
        if get_cell(fcs_result_path, 6, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 6, 10, sheet_name)
        data = eval(get_cell(fcs_result_path, 6, 6, sheet_name))
        html_name = data['htmlName']  # 转换后的预期标题名称
        driver.open_bro(url)
        name = driver.get_text("//*[@class='HD-title']")  # 转换后的实际标题名称
        assert name == html_name  # 验证转换后的实际标题名称等于预期的
        html_title = data['htmlTitle']  # 转换后html预期标签名称
        driver.open_bro(url)
        assert driver.get_title() == html_title  # 验证转换后html实际标签等于预期的