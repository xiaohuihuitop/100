"""
with open(file) as obj:
这种写法是python 提供的一种更加方便与安全的写法
可以在文件打开失败的时候 自动close
类似下方:
try:
    f = open('/path/', 'r')
    print(f.read())
finally:
    if f:

"""

Test_File = open(r"./测试文件IO.txt", mode='w+', encoding='utf8')
Test_File.write("写入测试数据  /// 不保留 \n//测试住宿///未消失  \n  ///删除 \n  //保留 \n  嘿嘿//保留  \n  嘿嘿/// 消失\n")
Test_File.close()

with open(r"./测试文件IO.txt", mode='a+', encoding='utf8') as Test_File:
    Test_File.write("写入测试数据 //保留\n //测试住宿///未消失  \n  ///删除 \n  //保留 \n  嘿嘿//保留  \n  嘿嘿/// 消失\n")

with open(r"./测试文件IO.txt", mode='r', encoding='utf8') as Test_File:
    Test_Str = Test_File.read(1024)
    print(Test_Str)

# with open(r"./测试文件IO.txt", mode='r+', encoding="utf8") as Test_File:
#     line_num = Test_File.tell()
#     Test_Str = str(Test_File.readline())
#     print("line_num:", line_num)
#     print(Test_Str, len(Test_Str))
#     target = Test_Str.find("//", 0, len(Test_Str))
#     print(target)
#     if target != -1:
#         if Test_Str[target + 2] == "/":  # 需要处理
#             New_Str = str(Test_Str[:target])
#             print(New_Str, len(New_Str))
#
#             Test_File.seek(line_num)
#
#             Test_File.write(New_Str + "-"*(len(Test_Str) - len(New_Str) + 4))  # 这里写了  但是没把原来的行清除  所以就好像没写一样
#
#         else:
#             pass
#     else:
#         pass


"""
    文本操作
    主要记录了 编码之间的转换与差异
    为了兼容性 推荐 utf8格式 和 二进制
    
    write 写入文件时 不会将未覆盖位置数据清除 没有按行写入的函数
"""

with open(r"./测试文件IO.txt", mode='rb+') as Test_File:
    while True:
        line_num = Test_File.tell()
        Test_Str = (Test_File.readline()).decode("utf-8")  # 读取得到的是二进制（unicode）需要解码为 utf8(字符串)
        if Test_Str == '':
            break
        # print("line_num:", line_num)
        # print(Test_Str, len(Test_Str.encode("utf-8")))
        target = Test_Str.find("//", 0, len(Test_Str))
        # print(target)
        if target != -1:  # 有找到 //
            if Test_Str[target + 2] == "/":  # 需要处理
                New_Str = str(Test_Str[:target])  # 只保留 // 前面的数据
                # print(New_Str, len(New_Str.encode("utf-8")))

                Test_File.seek(line_num)  # 移动到该行的起始位置
                Test_File.write(  # 写入数据和空格 如果不写入空格是没有效果的
                    (New_Str + " " * (len(Test_Str.encode("utf-8")) - len(New_Str.encode("utf-8")) - 1)).encode("utf-8")
                )

                # 测试  encode前后 Str长度差异 ---> 双倍 并且 没有计算 空格？
                # print(len(Test_Str.encode("utf-8")) - len(New_Str.encode("utf-8")) - 1 + len(New_Str))
                # Test_File.write(('{:<23}'.format(New_Str)).encode("utf-8"))
                # print(New_Str,len(New_Str),len(New_Str.encode("utf-8")))
            else:
                pass
        else:
            pass
