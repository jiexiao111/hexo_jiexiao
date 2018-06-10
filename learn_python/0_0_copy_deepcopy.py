import copy

# 原始对象
a = [1, 2, ['a', 'b']]
# 引用拷贝
b = a
# 浅拷贝
c = copy.copy(a)
# 深拷贝
d = copy.deepcopy(a)

# 变更 a
a.append(3)
a[2].append("c")

# 查看变化
print("a: ", a)
print("b: ", b)
print("c: ", c)
print("d: ", d)
