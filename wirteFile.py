import ast

import pymysql

from AllSequences import AllSequences
from Allbundle import Allbundle
from CompetitiveThree import CompetitiveThree
from Revenue import Revenue

"""
    这个函数是读写文件，然后以全排序的方式，返回拿取物品的所有序列，
    Agent_A文本是全排序文本
    ThreeAgent_A是A的拿取序列文本
    ThreeAgent_B是B的拿取序列文本
    ThreeAgent_C是C的拿取序列文本
    revenue是AgentA的收益文本
    R 是最后的显示文本
"""


class wirteFile:

    def write(agent_b, agent_c, bundle, num):

        # sequences_generator = AllSequences(num)
        # permutations = sequences_generator.permute()
        competition_three = CompetitiveThree(num)
        competition_a = [0] * num
        competition_b = [0] * num
        competition_c = [0] * num

        bundleSequence = Allbundle(set(bundle))
        bundleSequence.write_to_file("bundleSequence.text")
        # 读取Agent_A 的全排列
        with open('E:\\pydemo\\Agent\\bundleSequence.text', 'r') as file_2:
            for line in file_2:
                # 从Agent_A 文本中读取一行数据，即一种拿取顺序，并去除末尾‘\n'
                data = ast.literal_eval(line.rstrip('\n'))
                for i in range(num - len(bundle)):
                    data.append(0)
                # 调用三人竞争算法，生成每个agent 可能获得的物品
                # print(data)
                competition_three.competitive_n(data, agent_b, agent_c, competition_b, competition_c,
                                                competition_a, num)
                # 生成Agent A,B,C 的获得物品集
                with open('E:\\pydemo\\Agent\\ThreeAgent_A.txt', 'a') as file_3, \
                        open('E:\\pydemo\\Agent\\ThreeAgent_B.txt', 'a') as file_4, \
                        open('E:\\pydemo\\Agent\\ThreeAgent_C.txt', 'a') as file_5:
                    competition_a = [elem for elem in competition_a if elem != 0]
                    competition_b = [elem for elem in competition_b if elem != 0]
                    competition_c = [elem for elem in competition_c if elem != 0]
                    file_3.write(str(competition_a) + '\n')
                    file_4.write(str(competition_b) + '\n')
                    file_5.write(str(competition_c) + '\n')
                competition_b = [0] * num
                competition_c = [0] * num
                competition_a = [0] * num

        MaxValue = 0.00
        MaxVector = 0.0
        with (open('E:\\pydemo\\Agent\\ThreeAgent_A.txt', 'r') as file_agent_a1, \
              open('E:\\pydemo\\Agent\\ThreeAgent_B.txt', 'r') as file_agent_b1, \
              open('E:\\pydemo\\Agent\\ThreeAgent_C.txt', 'r') as file_agent_c1, \
              # open('E:\\pydemo\\Agent\\Agent_A.text', 'r') as file_agent_a2, \
              open('E:\\pydemo\\Agent\\result.txt', 'a') as file_result1):
            for line_a, line_b, line_c in zip(file_agent_a1, file_agent_b1, file_agent_c1):
                data_a = ast.literal_eval(line_a.rstrip('\n'))
                data_b = ast.literal_eval(line_b.rstrip('\n'))
                data_c = ast.literal_eval(line_c.rstrip('\n'))
                # data_a2 = ast.literal_eval(line_a2.rstrip('\n'))
                file_result1.write('bundle:' + str(bundle) + 'Bs:' + str(agent_b) + 'Cs:' + str(agent_c) + 'A:' + str(
                    data_a) + 'B:' + str(data_b) + 'C:' + str(data_c) + '\n')
                revenue = Revenue()
                res = [0] * len(data_a)
                vector = 0
                E, vector = revenue.compute_revenue(data_a, data_b, data_c, res, bundle, vector)
                if E > MaxValue:
                    MaxValue = E
                if vector > MaxVector:
                    MaxVector = vector
                with open('E:\\pydemo\\Agent\\revenue.txt', 'a') as file_agent_revenue:
                    file_agent_revenue.write(
                        "收益为： " + str(E) + " 收益向量为：" + str(res) + "收益矩阵为：" + str(vector) + '\n')
        with open('E:\\pydemo\\Agent\\result.txt', 'r') as file_agent_result, \
                open('E:\\pydemo\\Agent\\revenue.txt', 'r') as file_agent_revenue, \
                open('E:\\pydemo\\Agent\\R.txt', 'a') as file_agent_r:
            for line_3, line_4 in zip(file_agent_result, file_agent_revenue):
                file_agent_r.write(line_3.strip() + ' ' + line_4)

            # If one file is longer than the other, write the remaining lines
            for remaining_line in file_agent_result:
                file_agent_r.write(remaining_line)
        # 这是筛选出重复的策略
        with open('E:\\pydemo\\Agent\\R.txt', 'r') as file_agent_R, \
                open('E:\\pydemo\\Agent\\bundleSequence.text', 'r') as file_agent_A, \
                open('E:\\pydemo\\Agent\\res.txt', 'a') as file_agent_res:
            file_agent_A.seek(0)
            texts = set()
            for line in file_agent_R:
                texts.add(line)
            for text in texts:
                file_agent_res.write(text)
            # for line in file_agent_R:
            #     file_agent_res.write(line)
        # 读取文件内容并存储到列表中
        with open('E:\\pydemo\\Agent\\res.txt', 'r') as file_agent_res:
            lines = file_agent_res.readlines()

        # 将符合条件的行写入到目标文件中
        with open('E:\\pydemo\\Agent\\maxvalue.txt', 'a') as file_agent_maxvalue:
            print("最高收益为：" + str(MaxValue))
            for line in lines:
                index = line.find("收益为：")
                if index != -1:
                    data = float(line[index + 5:index + 9])
                    # print(data)
                    if data == MaxValue:
                        file_agent_maxvalue.write(line)
                # 将符合条件的行写入到目标文件中

        with open('maxvalue.txt', 'r') as file_agent_maxvalue:
            lines = file_agent_maxvalue.readlines()
        with open('M.text', 'a') as file_agent_maxvalue_text, \
                open('three_C.tesxt', 'a') as three_C_text, \
                open('temp1.txt', 'w') as temp2_text:
            # three_C.tesxt 这个文件是找到有一个物品是三人同时竞争的案例
            print("最高收益向量为：" + str(MaxVector))
            for line in lines:
                index = line.find("收益矩阵为：")
                if index != -1:  # 确保找到了"收益矩阵"
                    # 直接添加"收益矩阵"之后的字符串，不包含原始行
                    data = int(line[index + 6:])
                    # print(data)
                    if data == MaxVector:
                        file_agent_maxvalue_text.write(line)
                        temp2_text.write(line)
                        if (data - 1) % 10 == 0:
                            three_C_text.write(line)
        return MaxValue
