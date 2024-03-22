# -*- coding: utf-8 -*-
import ast

import ast

max_list = None
max_value = float('-inf')  # 初始化为负无穷大

with open('M.text', 'r') as file_agent_res:
    lines = file_agent_res.readlines()

    # 遍历文件中的每一行
    for line in lines:
        index = line.find("收益矩阵为：")
        if index != -1:  # 如果找到了包含特定字符串的行
            data_str = line[index + 6:].strip()
            data_list = ast.literal_eval(data_str)  # 将字符串转换为列表

            # 将字符串列表转换为整数列表
            data_list = [int(x) for x in data_list]

            # 检查该列表中的最大值
            current_max = max(data_list)

            # 如果当前列表中的最大值大于记录的最大值，则更新记录的最大值和列表
            if current_max > max_value:
                max_value = current_max
                max_list = data_list

# max_list 现在包含具有最大值的列表
print(max_list)
max_vector = max_list
with open('E:\\pydemo\\Agent\\test.text', 'a') as file_agent_res, \
        open('E:\\pydemo\\Agent\\M.text', 'r') as f:
    lines = f.readlines()
    print('最高收益向量为：' + str(max_vector))
    for line in lines:
        index = line.find("收益矩阵为：")
        if index != -1:  # 确保找到了"收益矩阵"
            # 直接添加"收益矩阵"之后的字符串，不包含原始行
            temp = ast.literal_eval(line[index + 6:].rstrip('\n'))
            if temp == max_vector:
                file_agent_res.write(line)

