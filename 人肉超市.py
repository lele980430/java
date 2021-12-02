print("欢迎光临小店")
A = [
    ["浙江人",120],
    ["宁波人",100],
    ["温州人",100],
    ["杭州人",200],
    ["广州人",300],
    ["福建人",250],
    ["四川人",150],
    ["成都人",120],
    ["北京人",99],
    ["河南人",140],
    ["超人",777],
    ["雷神",666],
    ["浩克",555],
    ["唐僧",999]
]
B = [] #购物车
C = 10000 #钱包
for i in enumerate(A):#枚举 列举商品
    print(i)
while True:
    D = input("请选择商品")
    # 判断字符串内是不是由数字组成
    if D.isdigit():
        D = int(D)
        if D < len(A):
            if A[D] in A:  #某个元素在某个容器里面
                B.append(A[D]) #添加商品进入购物车
                C = C - A[D][1]
                if C==0 :
                    print("您已经没有钱了，可以用阳寿来购买")
                    continue
                print("已选商品：",B)
        else:print("没有此商品，请重新输入")
    elif D == "q" or D == "Q":
        print("多谢惠顾小店")
        for a in enumerate(B):
            print(a)
        print("余额为：",C)
        break
    else:print("输入有误，请重新输入")
