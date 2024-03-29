import unittest
import api
from api.api_employee import AplEmployee
from tools.assert_common import assert_common

class TestEmployee(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 获取ApiEmployee()
        cls.api = AplEmployee()
    # 新增员工
    def test01_post(self,username="bj1701",mobile="13011112222",workNumber="88111"):
        # 调用新增接口
        r = self.api.api_post_employee(username,mobile,workNumber)
        print("新增员工后结果为:",r.json())
        # 提取user_id
        api.user_id = r.json().get("data").get("id")
        print("新增的员工id为:",api.user_id)
        # 断言
        assert_common(self,r)

    # 更新
    # def test02_put(self):
    #   pass
    #
    # 查询
    # def test03_get(self):
    #    pass
    # 删除

    def test04_delete(self):
        r = self.api.api_delete_employee(api.user_id)
        print("删除数据结果为:",r.json())
        assert_common(self,r)