#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
#########################################################################

# akcsum = []
# for i in range(1,5):
#     xx = input("输入排序数字:")
#     akcsum.append(xx)
# akcsum.sort()
# print(akcsum)

# a = "mark-9527"
# print(a.center(40,"-"))
# print(a.endswith("7"))  #判断结尾是不是
# print(a.find("5")) #字符查找，
# print(a.isdigit()) #是不是个整数
# print("355".isdigit())
#
# xx = ['alex', 'jack', '⿊姑娘', 'rain', 'eva', '狗蛋', '绿⽑', '鸡头']
# cc = ['9527','yy']
#
# print("'++++'".join(xx))
# print(xx)
# print(xx.extend("cc"))


##用户登陆失败并锁定#######################################################################
acccounts = {}
f = open("../venv/login.txt", "r")
for line in f:
    line = line.strip().split(",")
    acccounts[line[0]] = line
print(acccounts)
count = 0
while count < 2:
    user = input("Uername:").strip()
    if user not in acccounts:
        print("该用户未注册.....")
        break
    passwd = input("Password:").strip()
    if  passwd == acccounts[user][1]:
        print(f"Welcome{user}....登陆成功.....")
        exit()
    else:
        print("Wrong password.....")
    count += 1
    if count == 1:
        print(f"输错了{count}密码，需要锁定帐号{user}!!!!!!!!")
    acccounts[user][2] = "555555"
    f2 = open("../venv/login-22.txt", "w")
    for user,val in acccounts.items():
        line = ",".join(val) + "\n"
        f2.write(line)
    f2.close()
exit("bey..........")

##运行脚本传入替换字段及内容#######################################################################

# import sys
# print(sys.argv)
#
# old_str = sys.argv[1]
# new_str = sys.argv[2]
# filename = sys.argv[3]
#
# f = open(filename,"r+")
# data = f.read()
#
# old_str_count = data.count(old_str)
# print(old_str_count)
#
# new_data = data.replace(old_str,new_str)
# f.seek(0)
# f.truncate()
#
# f.write(new_data)
# f.close()
#
# print(f"成功替换字符'{old_str}'to '{new_str}',共'{old_str_count}'处......")

##打开一个文件写入内容#######################################################################
# f = open(file='/Users/mark/work-tools/python/staff.txt') # 若⽂件已存在，则覆盖
# # f.write("领导开始抽奖33333333333333333335\n")
# # f.write(xx)
# # print(f.readlines())
# for lien in f:
#     lien = lien.split()
#     heigent = int(lien[0])
#     weigent = int(lien[4])
#     if heigent >= 5:
#         print(lien,'------分隔符-------')
#         # print(f.readline()) # 读⼀⾏
#         # print('------分隔符-------')
# f.close()
# fx = open(file='/Users/mark/work-tools/python/staff.txt',mode='r')
# print(fx.readline()) # 读⼀⾏
# print('------分隔符-------')
# data = fx.read() # 读所有，剩下的所有
# print(data)
# fx.close()

##用户列表分组#######################################################################
#
# stu_list = [['李渊', 82], ['李世⺠', 7], ['侯君集', 5], ['李靖', 58], ['魏征',41], ['房⽞龄', 64], ['杜如晦', 65], ['柴绍', 94], ['程知节', 45], ['尉迟恭', 94],['秦琼', 54], ['⻓孙⽆忌', 85], ['李存恭', 98], ['封德彝', 16], ['段志⽞', 44], ['刘弘基', 18], ['徐世绩', 86], ['李治', 19], ['武则天', 39], ['太平公主', 57], ['⻙后',76], ['李隆基', 95], ['杨⽟环', 33], ['王勃', 49], ['陈⼦昂', 91], ['卢照邻', 70],['杨炯', 81], ['王之涣', 82], ['安禄⼭', 18], ['史思明', 9], ['张巡', 15], ['雷万春', 72], ['李⽩', 61], ['⾼⼒⼠', 58], ['杜甫', 27], ['⽩居易', 5], ['王维', 14],['孟浩然', 32], ['杜牧', 95], ['李商隐', 34], ['郭⼦仪', 53], ['张易之', 39], ['张昌宗', 61], ['来俊⾂', 8], ['杨国忠', 84], ['李林甫', 95], ['⾼适', 100], ['王昌龄',40], ['孙思邈', 46], ['⽞奘', 84], ['鉴真', 90], ['⾼骈', 85], ['狄仁杰', 62], ['⻩ 巢', 79], ['王仙芝', 16], ['⽂成公主', 13], ['松赞⼲布', 47], ['薛涛', 79], ['⻥⽞机', 16], ['贺知章', 20], ['李泌', 17], ['韩愈', 100], ['柳宗元', 88], ['上官婉⼉ 五代⼗国：朱温', 55], ['刘仁恭', 6], ['丁会', 26], ['李克⽤', 39], ['李存勖', 11],['葛从周', 25], ['王建', 13], ['刘知远', 95], ['⽯敬瑭', 63], ['郭威', 28], ['柴 荣', 50], ['孟昶', 17], ['荆浩', 84], ['刘彟', 18], ['张及之', 45], ['杜宇', 73],['⾼季兴', 39], ['喻皓', 50], ['历真', 70], ['李茂贞', 6], ['朱友珪', 7], ['朱友贞',11], ['刘守光', 2]]
# stu_group = [[11],[22],[88888],[99999],[44]]
# stu_group2 = []
# for i in stu_list:
#     if i[1] > 90:
#         stu_group[0].append(i)
#     elif i[1] > 80:
#         stu_group[1].append(i)
#     elif i[1] > 70:
#         stu_group[4].append(i)
#
# for xxx in stu_group:
#     print(xxx)


##智能客服监控脚本#######################################################################
###测试语句 1. 智能客服系统健康检查接口接入报警
# http://172.16.2.151:18000/health_check/api/task_engine  	    多轮检测
# http://172.16.2.151:18000/health_check/api/intent  			意图检测
# http://172.16.2.151:18000/health_check/api/faq     			标准问检测
# http://172.16.2.151:18000/health_check/api/chat  			    闲聊检测
# 返回字段：errorCode为204，表示检测成功，400表示检测失败”

##年会抽奖程序#######################################################################
# 张三科技有限公司有300员⼯，开年会抽奖，奖项如下：
# ⼀等奖 3名， 泰国5⽇游
# ⼆等奖6名，Iphone⼿机
# 三等奖30名，避孕套⼀盒
# 规则：
# 1. 共抽3次，第⼀次抽3等奖，第2次抽2等奖，第3次压轴抽1等奖
# 2. 每个员⼯限中奖⼀次，不能重复
# import random
# import string
#
# userid = []
# for i in range(0, 31):
#     username = "".join(random.sample(string.ascii_letters + string.digits, 9))
#     userid_c = f"工号ID:{username}"
#     userid.append(userid_c)
# w1 = random.sample(userid, 3)
# w2 = random.sample(userid, 6)
# w3 = random.sample(userid, 10)
#
# count = -1
# while True:
#     count += 0
#     if count <= 2:
#         award = int(input(("领导开始抽奖:")))
#         if award == 1:
#             print(f"恭喜三等奖人员:三等奖获得避孕套一盒，谢谢！！！\n{w3}")
#         elif award == 2:
#             print(f"恭喜二等奖人员:二等奖获得Iphone手机一部，谢谢！！！\n{w2}")
#         elif award <= 3:
#             print(f"恭喜一等奖人员:泰国4⽇游，谢谢！！！\n{w1}")
#             exit()
#         else:
#             print("输入错误，请重新输入，谢谢！！！")
#             exit()

##京牌摇号⼩程序1#######################################################################
# 需求：
# 1. 允许⽤户最多选3次
# 2. 每次放出20个⻋牌供⽤户选择
# 3. 京[A-Z]-[xxxxx], 可以是数字和字⺟在组合   京Q2H3t2
# 想实现这个程序 ，有2个问题要解决：
# 1. 如果实现输出随机值
# 2. 随机值需限定在⼤写字⺟，和数字范围内，不能有其它特殊字符。
# 这就要⽤到⼀些超纲知识， random模块和string模块。 Python的模块库是个宝藏，想实现任何功能它
# 都有现成的模块供你调⽤

# import random
# import string
# car_nums = []
# for i in range(3):
#     print(f"===================第一组车牌{i}========================")
#     for xx in range(1,6):
#         n1 = random.choice(string.ascii_uppercase)
#         n2 = "".join(random.sample(string.ascii_letters+string.digits,5))
#         car_c = f"京{n1}-{n2}"
#         car_nums.append(car_c)
#         print(xx,car_c)
#     choice = input("输入你喜欢的号：").strip()
#     if choice in car_nums:
#         print(f"恭喜，你输入车牌存在{choice}")
#         exit("Good luck.")
#     else:
#         print("Sorry,你输入不存在")

##京牌摇号⼩程序2#######################################################################

# import random
# import string
# count = 0
# while count < 3:
#     car_nums = []
#     for xx in range(6):
#         n1 = random.choice(string.ascii_uppercase)
#         n2 = "".join(random.sample(string.ascii_letters+string.digits,5))
#         car_c = f"京{n1}-{n2}"
#         car_nums.append(car_c)
#         print(xx,car_c)
#     choice = input("输入你喜欢的号：").strip()
#     if choice in car_nums:
#         print(f"恭喜，你输入车牌存在{choice}")
#         exit("Good luck.")
#     else:
#         print("Sorry,你输入不存在")
# count += 1

#########################################################################
# for i in range(10):
#     if i % 2 == 0:
#         print(f"{i}=========偶数" )
#     else:
#         print(f"{i}=====++++++++++++++=====奇数")

# 解题思路，10次循环，前5次打印 i * "*" , 后5次打印 (10-i) * "*"
# nn = 100
# for i in range(nn):
#     if i < 50:
#         print(i * "&")
#     else:
#         print( (nn-i) * "&")
#########################################################################
# for i in range(1,6):
#     print(f"++++++++++++++++第{i}部分++++++++++++++")
#     for ff in range(1,6):
#         # if  i == 3:
#         #     continue
#         if i == 4 or ff == 4:
#             print("跳过不吉利数字4的楼层")
#             continue
#         print(f"楼层号:L{i}-00{ff}-室")

##按如下格式打印99乘法表#######################################################################

# for i in range(1,10):
#     for xx in range(1,i+1):
#         print(f"{xx}x{i}={i*i}",end="  ")
#     print()

#########################################################################
# dd = 9
# for i in range(dd):
#     print( 1 x dd)

##猜你的年龄#######################################################################
# age_of_oldboy = 48
#
# for i in range(3):
# guess = int(input(">>:"))
# if guess > age_of_oldboy :
# print("猜的太⼤了，往⼩⾥试试...")
# elif guess < age_of_oldboy :
# print("猜的太⼩了，往⼤⾥试试...")
# else:
# print("恭喜你，猜对了...")

##查看工资是多少#######################################################################
# 你的⼯资多少决定了你的⼼态
# ⽉薪1000：⽼板，我是你爹。 ⽉薪2000：⽼板，wqnmlgbxxxx ⽉薪5000：⽼板脑⼦有坑，背
# 后说坏话。 ⽉薪1万：⽼板说的有有点问题，但我不说话。 ⽉薪2万：⽼板说啥就是啥吧，给钱就
# ⾏。 ⽉薪3万：⽼板说什么都是对，如果有⼈错了，那⼀定是我。 ⽉薪5万：996就像呼吸⼀样⾃
# 然。 ⽉薪10万：公司就是我家。

# gz = int(input("输入工资:"))
#
# if gz >= 90 and gz <= 100:
#     print("A")
#
# elif gz >= 80 and gz <= 89:
#     print("B")
#
# else:
#     print("你真笨！！！！！！")


#########################################################################

# httppath = ["task_engine","intent","fag","chat"]
# ipadd = "http://172.16.2.151:18000/health_check/api"
# health = 200
#
# username = str(input("输入你的姓名"))
#
# if username == "luxh":
#     print("你输入的是个大佬" * 10)
# else:
#     print("你输入的不正确")

#########################################################################
# list = ['runoob', 786, 2.23, 'john', 70.2]
# tinylist = [123, 'john']
#
# print (list)  # 输出完整列表
# print (list[0])  # 输出列表的第一个元素
# print (list[1:3])  # 输出第二个至第三个元素
# print (list[2:])  # 输出从第三个开始至列表末尾的所有元素
# print (tinylist * 2)  # 输出列表两次
# print (list + tinylist)  # 打印组合的列表

#########################################################################
# str = 'Hello World!'
# print (str)  # 输出完整字符串
# print (str[0])  # 输出字符串中的第一个字符
# print (str[2:5])  # 输出字符串中第三个至第六个之间的字符串
# print (str[2:])  # 输出从第三个字符开始的字符串
# print (str * 2)  # 输出字符串两次
# print (str + "TEST")  # 输出连接的字符串

#########################################################################