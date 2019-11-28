
#定义函数
def hanshu1(q,p):                     #()内为形参,调用函数时传入的位置实参 / 关键字实参会依次为其赋值
    print(str(q),str(q))
def hanshu2(q):
    q.pop()
    print(q)
#函数的拓展知识, 注意事项和妙用
#关键字实参
hanshu1(p=0,q=1)                      #此时会根据形参名, 一一对应地传入实参

#默认值
def hanshu3(q=0,p=0):                 #在函数定义时给形参赋值, 以达到给形参默认值的目的, 在调用函数时若实参数量不够或无对应关键字实参, 函数使用的形参会为默认值
    print(q+p)
hanshu3()                             #未传入任何实参

#等效的函数调用
#传入函数时是否使用关键字实参 / 是否使用形参默认值, 是等效的函数调用语句

#返回值
#return + 参数
#返回简单值(对字符串等数据的处理, 使之后对返回数据的处理更方便简单)
#返回字典(在函数中声明字典, 对参数进行封装, 一并传回)

#使实参变为可选
#将实参作为判断标准,如不符合某种标准,则进行另一套代码块

#传递列表/元组

#防止传入的列表被改变,可在调用函数时, 使用切片复制的方法产生临时列表并作为参数传入
q=[1,2,3,4,5]
print(hanshu2(q[:]))
print(hanshu2(q))
print(q)

#传递任意数量实参: def 函数名 (*形参名):
def hanshu4(*q):                        #将传入的所有实参存入形参(一个元组)中
    print(q)
#位置实参和任意数量实参的结合使用
def hanshu5(p,*q):                      #将传入的第一个实参存入第一个形参,其他所有实参存入形参(一个元组)中
    print(q)
#传入任意数量关键词实参                 
def hanshu6(a,b,**c):                   #" ** "符号表示建立一个空字典, 存入其中的实参键值对以 " xxx=xxx " 表示
    d={}                                #创建空字典用以存入形参的值
    d[1]='1'
    d[2]='2'
    d[3]='3'
    for key, value in c.items:          #将形参生成的字典中的键值对存入会被作为返回值的字典中
        d[key]=value
    return d

#将函数封装入一个 (py文件) 模块中
#在另一个py文件中调用整个模块 (import + py文件名)
#调用特定函数 (from + 函数模块名 + import + 函数名1,函数名2,函数名3)
#给模块指定别名 (import + py文件名 + as + 别名)
#导入一个模块中所有的函数 (from + 函数模块名 + import *)
