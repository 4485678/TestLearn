# 第一天 
安装pytest
pip install pytest -U #升级到最新版
启动 命令 pytest
代码 import pytest

pytest.main()

断言 assert 条件=true 正常往下走
条件=false 直接抛出 AssertionError，程序终止，提示测试失败。