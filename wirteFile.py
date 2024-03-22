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

    def wirte(agent_b, agent_c, bundle, num):

        # sequences_generator = AllSequences(num)
        # permutations = sequences_generator.permute()
        competition_three = CompetitiveThree(len(bundle))
        competition_a = [0] * len(bundle)
        competition_b = [0] * len(bundle)
        competition_c = [0] * len(bundle)
        # conn = pymysql.connect(  # 建立数据库的连接
        #     user='root',
        #     password='root',
        #     host='127.0.0.1',
        #     port=3307,
        #     database='msg'
        # )
        # cur = conn.cursor();
        # # 创建permutations表，这个表是用来收集全排列的数据
        # cur.execute('''
        #     CREATE TABLE IF NOT EXISTS permutations (
        #         id INT AUTO_INCREMENT PRIMARY KEY,
        #         permutation TEXT
        #     )
        # ''')
        # # 插入sql语句
        # for permutation in permutations:
        #     cur.execute('INSERT INTO permutations (permutation) VALUES (%s)', (str(permutation),))

        # 生成 Agent 的 全排列
        # with open('E:\\pydemo\\Agent\\Agent_A.txt', 'w') as file_1:
        #     for permutation in permutations:
        #         file_1.write(str(permutation) + '\n')
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
                competition_b = [0] * len(bundle)
                competition_c = [0] * len(bundle)
                competition_a = [0] * len(bundle)
        # cur.execute('SELECT COUNT(*) FROM permutations')
        # row_count = cur.fetchone()[0]  # Get the count of rows
        #
        # for flag in range(1, row_count + 1):
        #     cur.execute('SELECT permutation FROM permutations WHERE id = %s', (flag,))
        #     agent_a_data = ast.literal_eval(cur.fetchone()[0])  # Get the permutation value and parse it
        #     competition_three.competitive_n(agent_a_data, agent_b, agent_c, competition_b, competition_c, competition_a,
        #                                     num)
        #     # Perform any necessary processing or computations here
        #
        #     # Write the processed data back to the database
        #     try:
        #         cur.execute("INSERT INTO agent_a (data_a) VALUES (%s)", (str(competition_a),))
        #         cur.execute("INSERT INTO agent_b (data_b) VALUES (%s)", (str(competition_b),))
        #         cur.execute("INSERT INTO agent_c (data_c) VALUES (%s)", (str(competition_c),))
        #         conn.commit()  # Commit the changes
        #     except Exception as e:
        #         conn.rollback()  # Roll back the transaction in case of error
        #         print("Error:", e)
        # # Close the cursor and the database connection
        # cur.close()
        # conn.close()

        MaxValue = 0.0
        MaxVector = 0
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
                    data = float(line[index + 5:index + 8])
                    if data == MaxValue:
                        file_agent_maxvalue.write(line)
                # 将符合条件的行写入到目标文件中

        with open('maxvalue.txt', 'r') as file_agent_maxvalue:
            lines = file_agent_maxvalue.readlines()
        with open('M.text', 'a') as file_agent_maxvalue_text:
            print("最高收益向量为：" + str(MaxVector))
            for line in lines:
                index = line.find("收益矩阵为：")
                if index != -1:  # 确保找到了"收益矩阵"
                    # 直接添加"收益矩阵"之后的字符串，不包含原始行
                    data = int(line[index + 6:].rstrip('\n'))
                    if data == MaxVector:
                        file_agent_maxvalue_text.write(line)

        # with open('E:\\pydemo\\Agent\\maxvalue.txt', 'r') as file_agent_res:
        #     lines = file_agent_res.readlines()
        #
        #     # 初始化数据列表
        #     data = []
        #     for line in lines:
        #         index = line.find("收益矩阵为：")
        #         if index != -1:  # 确保找到了"收益矩阵"
        #             # 直接添加"收益矩阵"之后的字符串，不包含原始行
        #             data.append(line[index + 6:].strip())
        #
        #
        #     # 按照降序排序
        #     data.sort(reverse=True)
        #     max_vector = ast.literal_eval(data[0].rstrip('\n'))
        # with open('E:\\pydemo\\Agent\\M.text', 'a') as file_agent_res,\
        #         open('E:\\pydemo\\Agent\\maxvalue.txt', 'r') as f:
        #     lines = f.readlines()
        #     print('最高收益向量为：'+ str(max_vector))
        #     for line in lines:
        #         index = line.find("收益矩阵为：")
        #         if index != -1:  # 确保找到了"收益矩阵"
        #             # 直接添加"收益矩阵"之后的字符串，不包含原始行
        #             temp = ast.literal_eval(line[index + 6:].rstrip('\n'))
        #             if temp == max_vector:
        #                 file_agent_res.write(line)

        # max_list = None
        # max_value = float('-inf')  # 初始化为负无穷大
        #
        # with open('maxvalue.txt', 'r') as file_agent_res:
        #     lines = file_agent_res.readlines()
        #
        #     # 遍历文件中的每一行
        #     for line in lines:
        #         index = line.find("收益矩阵为：")
        #         if index != -1:  # 如果找到了包含特定字符串的行
        #             data_str = line[index + 6:].strip()
        #             data_list = ast.literal_eval(data_str)  # 将字符串转换为列表
        #
        #             # 将字符串列表转换为整数列表
        #             data_list = [int(x) for x in data_list]
        #
        #             # 检查该列表中的最大值
        #             current_max = max(data_list)
        #
        #             # 如果当前列表中的最大值大于记录的最大值，则更新记录的最大值和列表
        #             if current_max > max_value:
        #                 max_value = current_max
        #                 max_list = data_list
        #
        # # max_list 现在包含具有最大值的列表
        # max_vector = max_list
        # with open('E:\\pydemo\\Agent\\M.text', 'a') as file_agent_res, \
        #         open('E:\\pydemo\\Agent\\maxvalue.txt', 'r') as f:
        #     lines = f.readlines()
        #     print('最高收益向量为：' + str(max_vector))
        #     for line in lines:
        #         index = line.find("收益矩阵为：")
        #         if index != -1:  # 确保找到了"收益矩阵"
        #             # 直接添加"收益矩阵"之后的字符串，不包含原始行
        #             temp = ast.literal_eval(line[index + 6:].rstrip('\n'))
        #             if temp == max_vector:
        #                 file_agent_res.write(line)
