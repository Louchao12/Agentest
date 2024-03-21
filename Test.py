# -*- coding: utf-8 -*-


with open('E:\\pydemo\\Agent\\res.txt', 'r') as file_agent_res:
    lines = file_agent_res.readlines()

    # 初始化数据列表
    data = []
    for line in lines:
        index = line.find("收益矩阵")
        if index != -1:  # 确保找到了"收益矩阵"
            # 直接添加"收益矩阵"之后的字符串，不包含原始行
            data.append(line[index + 4:].strip())
            print(data[line])

    # 按照降序排序
    data.sort(reverse=True)

    # 如果最后两个元素不相等，找到最后一个相等的序列开始的位置并删除后面的所有元素
    if len(data) > 1 and data[-1] != data[-2]:
        last_value = data[-1]
        for i in range(len(data) - 2, -1, -1):
            if data[i] != last_value:
                del data[i + 1:]
                break

    # 将处理后的数据写入文件
    with open('E:\\pydemo\\Agent\\MaxValue.text', 'a') as file_maxvalue:
        for item in data:
            # 这里我们只有"收益矩阵"之后的字符串，没有原始行
            # 如果需要写入原始行，需要另外存储和处理
            file_maxvalue.write(item + '\n')  # 直接写入item，并添加换行符

