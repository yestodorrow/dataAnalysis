print("Hello Python")
# 交互界面窗口 输入输出交互式
# 编写和调试程序
# 语法词汇高亮显示
# 创建、编辑程序文件
print("hello world")

a=3
# 定时器
import time
time.sleep(3)
a=4
print(a)


print(a)


# 标量对象
# init 整数
# float 实数 16.0
# bool 布尔 True False
# NoneType 空类型
x="this is liu Gang"
y="he is a handsome boy"
print(x+","+y)


#变量
#赋值语句
x,y="liugang","very handsome"
sentence =x+" "+ y
print(sentence)

#注意：分隔符只能是英文的半角逗号

#数字的类型
  # 整数 浮点数 布尔型 复数（complex）
#   5+3j  complex(5,3）

# 判断数据类型
#  type() isinstance()
# print(type(5.0),type(1E+3),type())
#转换数据类型
# int() 转换成整数
print(int(3.9))
# print(int(3.9))
print(3>2>1)
#比较运算符
print(0)

#数学运算的优先级
print(x,y,x+y*3)
#字符串 同js

#输入函数
# 如何在交互中变量赋值呢
x=input("name")
print(x +" is very handsome")
# 注意 语句返回值为字符串，可以通过类型转换
x=input("4")
# print(x/4)
print(int(4)/4)
x=int(input("number"))
height=float(input("your savings in wechat or 支付宝"))
print(height)
print(x,sep=" ",end="\n")

print(x,y,sep="***",end="!")
