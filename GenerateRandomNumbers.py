import random


class GenerateRandomNumbers:
    def perfect_sequence(self, num):
        # 生成一个包含数字1到num的列表。
        arr = list(range(1, num + 1))
        # 使用Fisher-Yates算法对列表进行洗牌。
        for i in range(num - 1, 0, -1):
            # 生成一个随机索引，范围从0到当前循环变量i。
            index = random.randint(0, i)
            # 交换随机选定的元素和当前元素，实现洗牌效果。
            arr[index], arr[i] = arr[i], arr[index]
        return arr
