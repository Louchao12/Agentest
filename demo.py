import ast
import encodings

import generate_nonempty_power_set
from Allbundle import Allbundle
from GenerateRandomNumbers import GenerateRandomNumbers
from AllSequences import AllSequences
from CompetitiveSequence import CompetitiveSequence
from CompetitiveThree import CompetitiveThree
from Revenue import Revenue
from deleteFile import deleteFile
from thingsFirstPlace import thingsFirstPlace
from wirteFile import wirteFile

if __name__ == "__main__":
    num = 10
    # generator = GenerateRandomNumbers()
    # agent_b = generator.perfect_sequence(num)
    # agent_c = generator.perfect_sequence(num)
    # agent_b = [1, 2, 3, 4, 5, 6, 7, 8]
    # agent_c = [8, 7, 6, 5, 4, 3, 2, 1]
    bundle = {4, 2, 5, 3, 9, 1}
    bundleSequence = Allbundle(bundle)
    bundleSequence.write_to_file("bundleSequence.text")

    # print(agent_b)
    # print(agent_c)
    # 初始化competition_b和competition_c为列表

    # # 调用compete方法
    # competition_B = [0] * num
    # competition_C = [0] * num
    # competition_instance = CompetitiveSequence()
    # competition_instance.compete(agent_b, agent_c, competition_B, competition_C, num)
    #
    # # 清除0元素
    # competition_b = [elem for elem in competition_B if elem != 0]
    # competition_c = [elem for elem in competition_C if elem != 0]
    #
    # # 打印结果
    # print("Agent B 的比赛结果:", competition_b)
    # print("Agent C 的比赛结果:", competition_c)
    # 生成 Agent 的 全排列
    # sequences_generator = AllSequences(num)
    # permutations = sequences_generator.permute()
    # with open('E:\\pydemo\\Agent\\Agent_A.text', 'w') as file_1:
    #     for permutation in permutations:
    #       file_1.write(str(permutation) + '\n')
    with open('E:\\pydemo\\Agent\\bundleSequence.text', 'r') as file_a, \
            open('E:\\pydemo\\Agent\\Agent_B.tesxt', 'r') as copy_b, \
            open('E:\\pydemo\\Agent\\Agent_C.tesxt', 'r') as copy_c:
        # open('E:\\pydemo\\Agent\\bundle.tesxt', 'r') as bundle_writer:
        for line in copy_b:
            copy_c.seek(0)
            for line1 in copy_c:
                agent_b = ast.literal_eval(line.rstrip('\n'))
                agent_c = ast.literal_eval(line1.rstrip('\n'))
                # bundle = ast.literal_eval(bundle_line.rstrip('\n'))
                nums = wirteFile.wirte(agent_b, agent_c, bundle, num)
                deleteFile.delete_txt_files('E:\\pydemo\\Agent\\')
    # length = len(competition_b)
    # print(int(length / 2).__round__(0))
    # first_place = {}

    # num = 8
    #
    # find_first_place = thingsFirstPlace()
    # find_first_place.set_color(agent_b, agent_c, num, first_place)

    # for value in first_place.values():  # 找出目标物品第一次出现的位置
    #     print(value, end=" ")
    # value_list = [first_place.get(i) for i in bundle]
    # print("\n========================")
    # for value in value_list:
    #     print(value, end=" ")
    # print("\n========================")
    # value_list.sort(reverse=True)
    # for value in value_list:
    #     print(value, end=" ")
