import ast
# -*- coding: utf-8 -*-
import generate_nonempty_power_set
from AllSequences import AllSequences
from Allbundle import Allbundle
from deleteFile import deleteFile
from wirteFile import wirteFile

if __name__ == "__main__":
    # 总物品数
    num = 4
    # 生成全排序
    sequences_generator = AllSequences(num)
    permutations = sequences_generator.permute()
    # 将全排序写入文件，Agent_B是b的偏好
    with open('Agent_B.tesxt', 'w') as file_1:
        for permutation in permutations:
            file_1.write(str(permutation) + '\n')
    # 将文件B 复制一份给 C
    with open('Agent_B.tesxt', 'r') as file_2, \
            open('Agent_C.tesxt', 'w') as file_3:
        lines = file_2.readlines()
        for line in lines:
            file_3.write(str(line))
    # 生成目标物品
    bundle = [i for i in range(1, num + 1)]
    print(bundle)
    # 生成目标物品数超过总物品数一半的集合
    bundle_generator = generate_nonempty_power_set.generate_nonempty_power_set(bundle)
    # 将生成的序列写入文本
    with open("E:\\pydemo\\Agent\\bundle.tesxt", "w") as bundle_writer:
        for line in bundle_generator:
            bundle_writer.write(str(line) + '\n')

    with  open('E:\\pydemo\\Agent\\Agent_B.tesxt', 'r') as copy_b, \
            open('E:\\pydemo\\Agent\\Agent_C.tesxt', 'r') as copy_c, \
            open('E:\\pydemo\\Agent\\bundle.tesxt', 'r') as bundle_writer:

        for bundle_line in bundle_writer:
            # 将b文本回到第一行
            copy_b.seek(0)
            for line in copy_b:
                # 将c文本回到第一行
                copy_c.seek(0)
                for line1 in copy_c:
                    agent_b = ast.literal_eval(line.rstrip('\n'))  # 读取一条b的偏好
                    agent_c = ast.literal_eval(line1.rstrip('\n'))  # 读取一条c的偏好
                    bundle = ast.literal_eval(bundle_line.rstrip('\n'))  # 读取一条目标物品
                    nums = wirteFile.wirte(agent_b, agent_c, bundle, num)
                    deleteFile.delete_txt_files('E:\\pydemo\\Agent\\')
