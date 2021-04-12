import pytest
import yaml
from testing.counter import Calculator


def get_datas():
    with open("../datas/data_parm.yaml")as f:
        datas = yaml.safe_load(f)
        return datas


@pytest.fixture(params=get_datas()['data']['add'])
def login(request):
    yield request.param


@pytest.fixture(params=get_datas()['divs']['div'])
def divs(request):
    yield request.param


@pytest.fixture(scope='class')
def initcalc_class():
    print("setup")
    calc = Calculator()
    yield calc
    print("teatdown")
