# 导入pytest
import pytest

# 导入待测试的函数
from funcs import *


# 创建夹具（装饰器）
@pytest.fixture
def person():
    return Person("john", "doe")


# 测试函数1
def test__full_name(person):
    assert "John Doe" == person.full_name()


# 测试函数2
def test_last_name(person):
    assert "doe" == person.last_name
