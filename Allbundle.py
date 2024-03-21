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


if __name__ == '__main__':
    bundle = {1, 2, 3}
    bundlesequence = Allbundle(bundle)
    bundlesequence.write_to_file("bundle.txt")
