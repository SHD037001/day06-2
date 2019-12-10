# 导包
import unittest
import time
from tools.HTMLTestReportCN import HTMKTestRunner
# 定义测试套件
suite = unittest.defaultTestLoader.discover("./scripts")
# 获取报告存储文件流 并 实例化HtmlTestrunner 调用run
with open("./report/report.html","wb")as f:
    HTMKTestRunner(stream=f).run(suite)