""""
如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。

列表推倒式

语法：[最终结果 for 变量 in 可迭代对象 if 条件]

lst = [i for i in range(1,101) if i%2==0]

eval : eval() 函数用来执行一个字符串表达式，并返回表达式的值。
eval(expression[, globals[, locals]])   expression -- 表达式。

"""


def Is_Armstrong(parameter):
    temp_li = [eval(i) ** len(str(parameter)) for i in str(parameter)]  # 将每一位的次方结果存入列表
    if parameter == sum(temp_li):  # 列表元素相加 判断是否与原数据一致
        return parameter
    else:
        return None


# valid_num 从0到1000 中进行判断 ， 合符 if 判断的数据 加入到列表
Test_list = [valid_num for valid_num in range(0, 1000) if Is_Armstrong(valid_num) is not None]

print(Is_Armstrong(153))
print(Is_Armstrong(123))
print(Test_list)
