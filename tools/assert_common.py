import unittest

from api.api_login import ApiLogin
from tools.assert_common import assert_common


class TestLogin(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 获取ApiLogin对象
        cls.login = Apilpgin()

    # 登录测试方法
    def test01_login(self,mobile="13800000002",password= "123456"):
        # 调用业务方法
        r = self.login.api_login(mobile,password)