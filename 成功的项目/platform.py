import platform


print(platform.platform())  # 系统版本号
print(platform.version())
print(platform.architecture())  # 操作系统的位数
print(platform.machine())   # 计算机类型
print('node', platform.node())      # 计算机网络总称
print('processor++', platform.processor())     # 处理器信息
print(platform.uname())     # 包含上面所有的信息



print('222222222222222')

print(platform.system())

path = {'Windows', 'f:/fanchuang'}.get(platform.system())
print(path)