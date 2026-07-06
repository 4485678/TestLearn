import pytest
def test_add():
    # 预期1+1=2，断言成立，执行通过 .
    assert 1 + 1 == 2

def test_sub():
    # 预期5-2=1，断言成立，执行失败 .
    assert 5 - 2 == 1

@pytest.fixture()
def error_fixture():
    1 / 0

def test_error_case(error_fixture):
    assert True

@pytest.mark.skip(reason="跳过测试用例，暂不执行")
def test_skip():
    assert True

@pytest.mark.xfail()
def test_xfail():
    assert 2*3==6

@pytest.mark.xfail(reason="bug未修复，预期失败")
def test_xfail2():
    assert 2*3==5