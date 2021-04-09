import pytest
from testing.counter import Calculator


class TestOper:

    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    # 参数化加法
    @pytest.mark.parametrize('param1,param2,expect', [(1, 1, 2), (2, 2, 4), (3, 3, 6)], ids=['case1', 'case2', 'case3'])
    def test_add(self, param1, param2, expect):
        assert expect == self.calc.add(param1, param2)

    # 参数化除法
    @pytest.mark.parametrize('param1,param2,expect', [(10, 5, 2), (5, 5, 1)], ids=['case1', 'case2'])
    def test_div(self, param1, param2, expect):
        assert expect == self.calc.div(param1, param2)
