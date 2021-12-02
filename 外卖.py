'''
外卖小哥
一个外卖公司有三个分店
昌平一个三块，海淀五块，大兴十块昌平路远4个嵌套
有两个顾客
顺义和丰台

if I in dict_DZ["鄞州"]:
    print("ok")
'''
Q=0
dict_SP={"鄞州":{"钟公庙街道":{"万达广场":"谭鸭血","路费":7}}}
dict_DZ={"鄞州":{"钟公庙街道":{"堇悦雅庭":{"10幢":"405室"}}}}
while True:
    I = input("请输入地址")
    if I in dict_SP:
        I1 = input("请输入街道")
        if I1 in dict_SP[I]:
            I2 = input("请输入地址")
            if I2 in dict_SP[I][I1]:
                I3 = input("请输入商铺")
                if I3 in dict_SP[I][I1][I2]:
                    print("成功取到外卖")
                    print("开始送货")
                    Z = input("请输送货地址")
                    if Z in dict_DZ:
                        Z1 = input("请输送货街道")
                        if Z1 in dict_DZ[Z]:
                            Z2 = input("请输送货小区")
                            if Z2 in dict_DZ[Z][Z1]:
                                Z3 = input("请输几幢")
                                if Z3 in dict_DZ[Z][Z1][Z2]:
                                    print("送货成功")
                                    Q = Q + dict_SP[Z][Z1]["路费"]
                                    print("今日提成:",Q)
                else:print("输入有误，请重新输入")
            else:print("输入有误，请重新输入")
        else:print("输入有误，请重新输入")