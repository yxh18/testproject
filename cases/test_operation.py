import pytest
from testing.counter import Calculator


class TestOper:
    # 参数化加法
    # @pytest.mark.parametrize('param1,param2,expect',[(1,1,2),(2,2,4)])
    def test_add(self, initcalc_class, login):
        assert login[2] == initcalc_class.add(login[0], login[1])
    # 参数化除法
    # @pytest.mark.parametrize('param1,param2,expect', [(10, 0, 2), (5, 5, 1)], ids=['case1', 'case2'])

    def test_div(self, divs, initcalc_class):
        try:
            assert divs[2] == initcalc_class.div(divs[0], divs[1])
            print(divs)
        except ZeroDivisionError as e:
            print("除数不能为零")
