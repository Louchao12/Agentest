# -*- coding: utf-8 -*-
class Allbundle:
    def __init__(self, nums):
        self.nums = nums

    def permute(self, nums=None):
        if nums is None:
            nums = self.nums
        if len(nums) == 0:
            yield []
        else:
            for num in nums:
                rest = nums - {num}  # 去除当前数字
                rest_permutations = self.permute(rest)
                for perm in rest_permutations:
                    yield [num] + perm

    def write_to_file(self, filename):
        with open(filename, "w") as f:
            for permutation in self.permute():
                f.write(str(permutation) + "\n")

# if __name__ == '__main__':
#     with open("E:\\pydemo\\Agent\\bundle.text", "r") as bundle_reader:
#         for line in bundle_reader:
#             # 将读取的行解析为整数列表
#             bundle = set(map(int, line.strip().split(',')))
#             # 创建 Allbundle 实例并写入文件
#             bundlesequence = Allbundle(bundle)
#             bundlesequence.write_to_file("bundleSequence.txt")
