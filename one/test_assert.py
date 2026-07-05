# assert 判断表达式, "失败时自定义提示文字"

a = 1
assert a == 1
print("代码继续执行")

b = 2
assert a>b
# 等价于
assert 2 > 5

age = 15
assert age >= 18, "年龄必须满18岁"