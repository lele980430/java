from random import randint

print("==================")
print("|     中国银行    |")
print("==================")
print("|1、开户          |")
print("|2、存钱          |")
print("|3、取钱          |")
print("|4、转账          |")
print("|5、查询          |")
print('|6、退出          |')
bank = {'1': {'account_number': "1", 'password': "1", 'country': '1', 'province': '1', 'street': '1', 'door': '1',
              'bank_name': '中国银行', 'money': 1000},
        '2': {'account_number': "2", 'password': "2", 'country': '2', 'province': '2', 'street': '2', 'door': '2',
              'bank_name': '中国银行', 'money': 2000}}
bank_name = "中国工商银行"
# bank={'Frank': {'account': 29073386, 'password': '123456', 'country': '中国', 'province': '山东', 'street': '1大街', 'door': '001', 'bank_name': '中国银行', 'money': 0}
def useradd():  # 定义方法————用来添加用户的
    account_number = randint(1000000, 99999999)
    username = input("请输入您的姓名")
    password = input("请输入您的密码")
    country = input("\t\t请输入您的国家")  # \t表示一个tab
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入你的街道")
    door = input("\t\t请输入您的门牌号")
    gift = bankadd(account_number, username, password, country, province, street, door)  # 位置对应
    print(bank)
    if gift == "1":
        print("开户成功,以下是您的详细信息")
        information = '''
        --------工商银行-------
            1、账号：%s
            2、姓名：%s
            3、密码：******
            4、国家：%s
            5、省份：%s
            6、街道：%s
            7、门牌：%s
            8、余额：%s
        '''
        print(information % (account_number, username, country, province, street, door, bank[username]["money"]))
    elif gift == "2":
        print("用户已存在")
    elif gift == "3":
        print("数据库已满")
def bankadd(account_number, username, password, country, province, street, door):
    if username in bank:  # 姓名在不在bank的键里
        return "2"
    elif len(bank) > 100:
        return "3"
    bank[username] = {
        "account_number": account_number,  # 从useradd的account获取的随机数
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "bank_name": bank_name,
        "money": 0}
    return "1"
#存钱
def save(yh,xj):
    if yh in bank:
        bank[yh]['money']=xj + bank[yh]['money']
        print("余额为："+str(bank[yh]['money']))
    else:return "No"
#取钱
def quqian(zx,zc,zv):
    if zx in bank:
        if zc in bank[zx]['password']:
            bank[zx]['money']=bank[zx]['money']-zv
            print('账户余额:',bank[zx]['money'])
        else:return "1"
    else:return  "2"
#转账
def zhuanzhang(zz,zz1,zz2):
    if zz in bank:
        if zz1 in bank:
            if bank[zz]['money'] > zz2:
                bank[zz]['money']=bank[zz]['money']-zz2
                bank[zz1]['money']=bank[zz1]['money']+zz2
                print('转出成功，账户余额：',bank[zz]['money'])
            else:return '1'
        else:return '2'
    else:return '3'
#查询
def chaxun(cx,cx1):
    if cx in bank:
        if cx1 in bank[cx]['password']:
            information='''
        --------工商银行-------
            1、账号：%s
            2、姓名：%s
            3、密码：******
            4、国家：%s
            5、省份：%s
            6、街道：%s
            7、门牌：%s
            8、余额：%s
        '''
            print(information % (bank[cx]['account_number'], cx, bank[cx]['country'], bank[cx]['province'], bank[cx]['street'], bank[cx]['door'],
            bank[cx]["money"]))
        else:return '3'
    else:return '2'

while True:
    DL = input("请输入需要办理的业务")
    if DL == "1":
        print("正在为您开户")
        useradd()
    elif DL == "2":
        print("存钱")
        yh = input("输入用户名")
        xj = int(input("输入存钱数额"))
        sj=save(yh,xj)
        if sj=="No":
            print("输入有误")
    elif DL == "3":
        print("取钱")
        zx=input("输入用户名")
        zc=input("输入密码")
        zv=int(input("输入取钱数额"))
        sj1=quqian(zx,zc,zv)
        if sj1=="2":
            print("账户错误")
        if sj1=='1':
            print('密码错误')
    elif DL == "4":
        print("转账")
        zz=input('输入账户')
        zz1=input('输入转出账户')
        zz2=int(input('输入转账金额'))
        zz3=zhuanzhang(zz,zz1,zz2)
        if zz3=='3':
            print('账户错误')
        elif zz3=='2':
            print('转出账户错误')
        elif zz3=='1':
            print('余额不足')
    elif DL == "5":
        print("查询")
        cx=input('输入用户名')
        cx1=input('输入密码')
        cx4=chaxun(cx, cx1)
        if cx4=='2':
            print('账户错误')
        elif cx4=='3':
            print('密码错误')
    elif DL == "6":
        print("再见")
        continue

