import pytest
from main import BrowserAction
from time import sleep
from tools import *

driver = BrowserAction()
pro_path = os.path.dirname(os.path.dirname(__file__))
path = get_conf('FCS', '测试结果文件夹')
fcs_result_path = pro_path + "/" + path
sheet_name = '功能参数'


class TestCase:

    def test_ZMYF_8551(self):
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
        file_path = get_download_path() + '\\' + file_name
        assert get_excel_content(file_path, 1, 1, 'Sheet1') == "干部花名册报表(2021年03月09日)"

    def test_ZMYF_8888_1(self):
        if get_cell(fcs_result_path, 7, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 7, 10, sheet_name)
        print(url)
        driver.open_bro(url)
        driver.element_input("//input[@id='currentPage']", 9, clear=2)
        sleep(5)
        driver.screenshot_save(7, sheet_name)

    def test_ZMYF_9250(self):
        if get_cell(fcs_result_path, 12, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 12, 10, sheet_name)
        print(url)
        driver.open_bro(url)
        driver.element_input("//input[@id='currentPage']", 20, clear=2)
        driver.screenshot_save(12, sheet_name)

    def test_ZMYF_9266(self):
        if get_cell(fcs_result_path, 13, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 13, 10, sheet_name)
        print(url)
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
        driver.move_click(driver.find_ele("//*[@id='content']"))  # 移动到签批文本框左侧100单位
        sleep(1)
        driver.click_ele("//div[@class='save']")  # 点击保存
        sleep(2)
        driver.element_input("//input[@id='currentPage']", 2, clear=2)
        driver.screenshot_save(13, sheet_name)

    def test_ZMYF_9310(self):
        if get_cell(fcs_result_path, 14, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 14, 10, sheet_name)
        print(url)
        driver.open_bro(url)
        driver.screenshot_save(14, sheet_name)

    def test_ZMYF_9328(self):
        if get_cell(fcs_result_path, 16, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 16, 10, sheet_name)
        # print(url)
        driver.open_bro(url)
        del_download_file()  # 删除下载目录,重新新建
        file_name = driver.get_text("//span[@class='title']")  # 获取文件名
        driver.ele_exist("//img[@title='下载']")  # 验证参数为1时，有“下载”按钮存在
        driver.click_ele("//img[@title='下载']")
        sleep(2)
        assert (download_file_exist(file_name))  # 验证项目download文件夹下有该文件

    def test_ZMYF_9606(self):
        if get_cell(fcs_result_path, 22, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 22, 10, sheet_name)
        # print(url)
        driver.open_bro(url)
        del_download_file()  # 删除下载目录,重新新建
        file_name = driver.get_text("//span[@class='title']")  # 获取文件名
        driver.ele_exist("//img[@title='下载']")  # 验证参数为1时，有“下载”按钮存在
        driver.click_ele("//img[@title='下载']")
        sleep(2)
        assert (download_file_exist(file_name))  # 验证项目download文件夹下有该文件

    def test_ZMYF_8733(self):
        if get_cell(fcs_result_path, 29, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 29, 10, sheet_name)
        # print(url)
        driver.open_bro(url)
        assert (driver.get_text("//span[@title='总页数']")) == '6'

    def test_ZMYF_9160(self):
        if get_cell(fcs_result_path, 30, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 30, 10, sheet_name)
        # print(url)
        driver.open_bro(url)
        assert (driver.get_text("//span[@title='总页数']")) == '4'

    def test_ZMYF_9903(self):
        if get_cell(fcs_result_path, 32, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 32, 10, sheet_name)
        # print(url)
        driver.open_bro(url)
        assert (driver.get_text("//span[@title='总页数']")) == '1'

    def test_ZMYF_9372(self):
        assert get_cell(fcs_result_path, 36, 9, sheet_name) == '通过'

    def test_ZMYF_9486(self):
        assert get_cell(fcs_result_path, 37, 9, sheet_name) == '通过'

    def test_ZMYF_9503(self):
        assert get_cell(fcs_result_path, 37, 9, sheet_name) == '通过'

    def test_ZMYF_9906(self):
        if get_cell(fcs_result_path, 52, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 52, 10, sheet_name)
        driver.open_bro(url)

    def test_ZMYF_3771(self):
        assert get_cell(fcs_result_path, 55, 9, sheet_name) == '通过'

    def test_ZMYF_3800(self):
        if get_cell(fcs_result_path, 56, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 56, 10, sheet_name)
        driver.open_bro(url)
        assert driver.get_text("//div[@id='sheet-10']/span") == "互联网工作量测算"

    def test_ZMYF_8751_1(self):
        assert get_cell(fcs_result_path, 60, 9, sheet_name) == '通过'

    def test_ZMYF_9260(self):
        assert get_cell(fcs_result_path, 64, 9, sheet_name) == '通过'

    def test_ZMYF_9262_2(self):
        assert get_cell(fcs_result_path, 66, 9, sheet_name) == '通过'

    def test_ZMYF_9365(self):
        assert get_cell(fcs_result_path, 68, 9, sheet_name) == '通过'

    def test_ZMYF_9498(self):
        assert get_cell(fcs_result_path, 69, 9, sheet_name) == '通过'

    def test_ZMYF_9261(self):
        assert get_cell(fcs_result_path, 71, 9, sheet_name) == '通过'

    def test_ZMYF_10056(self):
        assert get_cell(fcs_result_path, 73, 9, sheet_name) == '通过'
