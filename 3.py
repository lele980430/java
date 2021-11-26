#sum()求和  map（）应用于序列的内置函数第一个参数接受一个函数名，后面的参数接受一个或多个可迭代的序列，返回的是一个集合
#strip（）用于去除字符串的首位字符 split()拆分字符串
# print(sum(map(int,input("请输入一组数字：").strip(',').split(',')))) #输入一组数字求和
# 1.实现输入10个数字，并打印10个数的求和结果

# i=1
# a=0
# while i<=10:
#     b=int(input("请输入第"+str(i)+"个数字："))
#     print(b)
#     i=i+1
#     a=b+a
# print("10个数的和1为：",a)


'''
2.键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数
'''
# i=10
# a=0
# c=[]
# while True:
#     b=int(input("请输入"+str(i)+"个数："))
#     c.append(int(b))
#     d=a/10
#     i=i-1
#     a=b+a
#     if i == 0:
#         print("合为：",a)
#         print("最大值为：",max(c))
#         print("平均值为:",a)
#         break


'''
3.使用random模块，如何产生 50~150之间的数？
'''
# import random
# a = random.randint(50,150)
# print(a)


'''
4.从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
'''
# A=10
# import math
# while True:
#     a=int(input("请输入a的边长:"))
#     b=int(input("请输入b的边长:"))
#     c=int(input("请输入c的边长:"))
#     if a + b > c and a + c > b and b + c > a:
#         print("可以构成三角形")
#     else:
#         continue
#     D=(a*a)
#     B=(b*b)
#     C=(c*c)
#     if B + C == D and B + D == C and C + D == B:
#         print("构成直角三角形")
#     if B + C < D and B + D < C and C + D < B:
#         print("构成钝角三角形")
#     if B + C > D and B + D > C and C + D > B:
#         print("构成锐角三角形")
#     print("角a：",a,"角b：",b,"角c：",c)
#     break



'''
5.有以下两个数，使用+，-号实现两个数的调换。
A=56
B=78
实现效果：
A=78
B=56

'''
# A=[56]
# B=[78]
# a.pop()
# b.pop()
# a.append(78)
# b.append(56)
# print(a)
# print(b)
'''
6.实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
'''
# import time#导入睡眠模块
# q=3
# HU="root"
# MI="admin"
# while True:
#     b=input("请输入用户名：")
#     a=input("请输入密码：")
#     if MI != a and HU != b:
#         q=int(q-1)
#         print("还剩",q,"次机会")
#         if q==0:
#             e.append(HU)
#             print("账号已锁定")
#             time.sleep(10000)#睡眠10000秒
#     else:
#         print("登录成功！")

'''
7、编程实现下列图形的打印
'''
# print("      *")
# print("     * *")
# print("    * * *")
# print("   * * * *")
# print("  * * * * *")
# print(" * * * * * *")
# print("* * * * * * *")

'''
使用while循环实现NxN乘法表的打印。
'''
# def f(N):
#     i = 1
#     while i<= N:
#         j = 1
#         while j<= i:
#             print("%d*%d=%d\t" %(j,i,j*i),end="\t")
#             j += 1
#         print()
#         i += 1
# N= int(input("请输入N的值："))
# f(N)


# for i in range(1,9+1):
#     for j in range(1,i+1):
#         print("%d*%d=%d\t" %(j,i,j*i),end="")
#     print()


'''
一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
'''
# j=20
# p=3
# h=2
# t=0
# while True:
#     j=j-p
#     t=t+1
#     if j == 0:
#         print(t)
#         break
#     j=j+h
#     if j == 0:
#         print(t)
'''
判断下列变量命名是否合法
标识符	是否合法	标识符	是否合法
char		    Cy%ty	
Oax_li		    $123	
fLul		    3_3 	
BYTE		    T_T	
'''
# while True:
#     s = input('变量名：')
#     if s[0].isalpha() or s[0] == '_':
#         for i in s[1:]:
#              if not(i.isalnim()or i =='_'):
#                 print('%s变量名不合法'%s)
#                 break
#         else:
#             print('%s变量名合法'%s)
#     else:print('%s变量名不合法'%s)
#
#
#
# # while True:
# #     a = input(i.pop())
# #     if a == 'exit':
# #         print("欢迎下次使用")
# #         break

'''
继续完成上午的猜数字游戏的需求功能。 
+
1.	添加计数打印功能
2.	添加次数金币功能和锁定系统功能。

'''
# import random#导入模块
# import time
# money=5000
# I=15
# B=0
# print("持有现金:",money)
# T = random.randint(1, 20)
# while True:#这是一个循环
#     print("正确答案:",T)
#     E=input("请输入一个1-20的数字")
#     E=int(E)
#     if T == E:
#         print("BING")
#         money=money+3000
#         print("持有现金:",money)
#         T = random.randint(1, 20)
#         continue
#     else:
#         print("Try Again")
#         money=money-100
#         I=I-1
#         print("持有现金:",money)
#         print("剩余次数:",I)
#         if T > E:
#             print("猜小了")
#         else:
#             print("猜大了")
#     if I == B:
#         print("GAME OVER")
#         time.sleep(10000)  # 睡眠10000秒


'''
用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
'''
# def f(N):
#     i = 1
#     while i<= N:
#         j = 1
#         while j<= i:
#             print("%d*%d=%d\t" %(j,i,j*i),end="\t")
#             j += 1
#         print()
#         i += 1
# N= int(input("请输入N的值："))
# f(N)