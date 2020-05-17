# eval将字符串强制转化成表达式
a="123"
print(eval(a)+10)

# str

m=eval(a)+10
newStr=str(m)+"heLlo"
print(newStr)
print(newStr.upper(),newStr.lower())
print(newStr.capitalize())

for i in newStr:
    print(i)

