from AllSequences import AllSequences
from deleteFile import deleteFile

import itertools
import random

# -*- coding: utf-8 -*-
import random


class CreatPerfect:
    @staticmethod
    def write_random_permutations(num_permutations, filename):
        num = 8
        nums = list(range(1, num + 1))  # 生成 1 到 20 的列表
        with open(filename, "w") as f:
            # 逐个生成排列并写入文件
            for _ in range(num_permutations):
                permutation = random.sample(nums, len(nums))  # 随机排列
                f.write(str(permutation) + "\n")


if __name__ == "__main__":
    CreatPerfect.write_random_permutations(1000, "Agent_C.tesxt")

if __name__ == "__main__":
    n = 8
    num_list = [i for i in range(1, n + 1)]
    with open("Agent_B.tesxt", "w") as f:
        f.write(str(num_list) + '\n')
