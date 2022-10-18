from time import sleep

from fcs_review_run import get_except_screen_shoot, result_run
from tools import get_conf, get_sheet_name

# sheet_names = ['预览质量']


class TestCase:

    def test_ZMYF_001(self):
        # fcs_result_path = get_conf('FCS', '测试结果文件夹')
        # sheet_names = get_sheet_name(fcs_result_path)  # 获得该excel表下所有工作表
        get_except_screen_shoot()  # 期望截图
        sleep(5)
        result_run()  # 实际截图并对比
