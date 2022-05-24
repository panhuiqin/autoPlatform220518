# -*- coding:utf-8 -*-

# import pandas
#
# # 读取Excel
# file = pandas.read_excel(r'C:\Users\Administrator\Desktop\test.xlsx')
# # 获取列
# pet_ls = list(file['宠物'])
#
# num = 0
#
# for pet in pet_ls:
#     num = num + 1
#     print(num)
#     # f = file[file['宠物'] == pet]
#     # f.to_excel(r'C:\Users\Administrator\Desktop\{}.xlsx'.format(pet),index=False)
import time

print(time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
