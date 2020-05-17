# 有序的序列：字符串列表元组
# 索引 分片 加 乘
# 检查是否属于序列
# 长度 最大 最小
# print("hello")

# 列表 最灵活的对象类型
# 创建：方括号 逗号
a_list=["a",1,[1,2,3]]
for i in a_list:
    if type(i)=="<class 'list'>":
         print(type(i))
         for m in i :
             print(m)
    else:
        print(i)




# 转化为list
m=list("good")
print(m)


z=list(range(2,9))
print(z)


# 增删改查元素 类型转化 内置函数

n=m[1:3]
print(n)
print("d" in m,"z" not in z)
print(list("good").count("o"))


z=list()
z.append("m")
print(z)
z.extend(list("good"))
print(z)
z.insert(1,"n")
print(z)
z.insert(1,"boy")
print(z)
del z[0]
print(z)
# z.remove("o")
print(z)
h=z.pop()
# z.extend([1,23])
print(h,2222)
for i in z:
    print(i)


print(max(z))
z=[1,3,3,444,4]
print(z.sort(),z,z.reverse(),z)
z