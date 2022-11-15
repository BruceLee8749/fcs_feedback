import pytest
from selenium.webdriver import Keys

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

    def test_ZMYF_10058(self):
        if get_cell(fcs_result_path, 34, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 34, 10, sheet_name)
        driver.open_bro(url)
        driver.click_ele("//span[@class='fcon ico_file_dir']")
        sleep(2)
        driver.click_ele("//span[@class='fcon ico_file_dir']")
        driver.click_ele("//span[contains(text(),'.doc')]")
        sleep(1)
        driver.driver.switch_to.frame(driver.find_ele("//iframe[@class='pica-player pica-frame scroll']"))
        driver.element_input("//input[@id='currentPage']", 41, clear=2)
        driver.screenshot_save(34, sheet_name)

    def test_ZMYF_9655(self):
        if get_cell(fcs_result_path, 35, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 35, 10, sheet_name)
        driver.open_bro(url)
        driver.click_ele("//span[@class='fcon ico_file_dir']")
        sleep(1)
        driver.click_ele("//span[@class='fcon ico_file_doc']")
        sleep(1)
        driver.driver.switch_to.frame(driver.find_ele("//iframe[@class='pica-player pica-frame scroll']"))
        driver.element_input("//input[@id='currentPage']", 29, clear=2)
        driver.screenshot_save(35, sheet_name)

    def test_ZMYF_8878(self):
        assert get_cell(fcs_result_path, 40, 9, sheet_name) == '通过'

    def test_ZMYF_9156(self):
        assert get_cell(fcs_result_path, 41, 9, sheet_name) == '通过'

    def test_ZMYF_9219(self):
        if get_cell(fcs_result_path, 42, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 42, 10, sheet_name)
        driver.open_bro(url)
        driver.click_ele("//span[contains(text(),'.mp4')]")
        sleep(1)
        driver.driver.switch_to.frame(driver.find_ele("//iframe[@class='pica-player pica-frame scroll']"))
        driver.ele_exist("//div[@id='playerBtn']")

    def test_ZMYF_10096(self):
        assert get_cell(fcs_result_path, 46, 9, sheet_name) == '通过'

    def test_ZMYF_10233(self):
        if get_cell(fcs_result_path, 52, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 52, 10, sheet_name)
        driver.open_bro(url)
        driver.click_ele("//span[@class='fcon ico_file_dir']")
        sleep(1)
        driver.click_ele("//span[contains(text(),'兼容性')]")
        sleep(1)
        driver.driver.switch_to.frame(driver.find_ele("//iframe[@class='pica-player pica-frame scroll']"))
        driver.element_input("//input[@id='currentPage']", 50, clear=2)
        driver.screenshot_save(52, sheet_name)

    def test_YUP_2615(self):
        if get_cell(fcs_result_path, 53, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 53, 10, sheet_name)
        driver.open_bro(url)
        driver.click_ele("//span[@class='fcon ico_file_dir']")
        sleep(1)
        driver.click_ele("//span[contains(text(),'大小8')]")
        sleep(1)
        # driver.driver.switch_to.frame(driver.find_ele("//iframe[@class='pica-player pica-frame scroll']"))
        driver.screenshot_save(53, sheet_name)

    def test_YUP_2617(self):
        if get_cell(fcs_result_path, 54, 9, sheet_name) != '通过':
            pytest.skip("url转换失败,不执行该case")
        url = get_cell(fcs_result_path, 54, 10, sheet_name)
        driver.open_bro(url)
        assert driver.get_text("//span[@class='fname']") == '压缩文件解压有问题'
