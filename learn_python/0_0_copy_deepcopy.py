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

# NOTE 运算符 * 执行的是浅拷贝
tmp = [0] * 3
tmp[0] = 3
print("Set tmp[0]:", tmp)

tmp = [[0] * 3] * 3
tmp[0][0] = 3
print("Init with *, Set tmp[0][0]:", tmp)

tmp = [[0 for col in range(3)] for row in range(3)]
tmp[0][0] = 3
print("Init with range, Set tmp[0][0]:", tmp)
