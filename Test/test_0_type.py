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

    def test_convert0_001(self):
        if get_cell(fcs_result_path, 2, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 2, 10, sheet_name)
        print(url)
        driver.open_bro(url)
        del_download_file()  # 删除下载目录,重新新建
        file_name = driver.get_text("//div[@class='title___gzxbE']")  # 获取文件名
        driver.ele_exist("//img[@title='下载']")  # 验证参数为1时，有“下载”按钮存在
        driver.click_ele("//img[@title='下载']")
        sleep(2)
        assert (download_file_exist(file_name))  # 验证项目download文件夹下有该文件