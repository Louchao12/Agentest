# -*- coding: utf-8 -*-
import ast

import ast

import ast

# 读取文件并提取数据写入到 sort.txt 文件中
with open('M.text', 'r') as file_agent_maxvalue:
    lines = file_agent_maxvalue.readlines()

with open('sort.text', 'a') as file_agent_maxvalue_text:
    for line in lines:
        index = line.find("A:")
        if index != -1:  # 确保找到了 "A："
            data = line[index + 2:index + 14]
            file_agent_maxvalue_text.write(data + '\n')  # 将提取的内容写入到 sort.txt 中

# 读取 sort.txt 文件并进行排序
with open('sort.text', 'r') as file_agent_maxvalue_text:
    lines = file_agent_maxvalue_text.readlines()
    sorted_lines = sorted(lines)
    for line in sorted_lines:
        print(line.strip())  # 打印排序后的结果