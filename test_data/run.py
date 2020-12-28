
# 引入函数
from python1222.note7 import read_case,api_fun,write_result

'''
1、excel测试用例准备ok,代码可以自动读取用例数据------read_case(filename,sheetname)
2、执行接口测试，得到响应结果-------api_fun(url,data)
3、断言：响应结果==预期结果   ----通过/不通过？
4、写到 最终执行通过与否的结果-----write_result(filename,sheetname,row,column,final_result)

'''

import openpyxl
import requests
import jsonpath

# 将这整个过程封装，定义成一个函数：
def execute_fun(filename,sheetname):
    # 写入测试结果
    cases = read_case(filename,sheetname)         # 调用函数，设置变量接收返回值
    for case in cases:                                    # ---此处获取的都是str格式
        case_id = case['case_id']
        url = case['url']                         # 获取url的值
        data = eval(case['data'])                 # 获取data的值,使用eval运行出里面的dict格式
        expected = eval(case['expected'])         # 获取期望值,使用eval运行出里面的dict格式
        expect_msg = expected['msg']              # 获取预期中的msg

    # eval（） --- 运行被字符串包裹着的表达式
    # '{"mobile_phone": "18362980328", "pwd": "lemon666", "type":"1","reg_name":"小安"}'  # 字符串
    # dict0 = eval('{"mobile_phone": "18362980328", "pwd": "lemon666", "type":"1","reg_name":"小安"}')
    # print(dict0)
    # print(type(dict0))
    # print(eval('2+6'))

    # 执行测试用例
        real_result = api_fun(url,data)                    # 调用函数，执行测试用例
        real_msg = real_result['msg']
        # print(case_id,expect_msg,real_msg)

    # 断言
        if expect_msg == real_msg:
            print('第{}条用例执行通过'.format(case_id))
            final_re = 'passed'
        else:
            print('第{}条用例执行不通过'.format(case_id))
            final_re = 'failed'
        print('*'*20)                                       # 分隔增加阅读性

    # 写入测试结果
        write_result(filename,sheetname,case_id+1,8,final_re)

# 调用这个函数：
execute_fun('C:\\XiaoAn\\test_data\\test_case_api.xlsx', 'register')
execute_fun('C:\\XiaoAn\\test_data\\test_case_api.xlsx', 'login')
