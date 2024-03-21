class AllSequences:
    def __init__(self, num):
        self.num = num
        self.item = []
        self.initialize_items()

    def initialize_items(self):
        # 初始化 item 数组，默认传入喜欢所有物品
        self.item = list(range(1, self.num + 1))

    def permute(self):
        result = []
        self.generate_permutations(0, result)
        return result

    def generate_permutations(self, index, result):
        if index == self.num - 1:
            # 当前排列完成，将其添加到结果列表中
            permutation = list(self.item)
            result.append(permutation)
        else:
            # 递归生成排列
            for i in range(index, self.num):
                # 交换当前元素与起始索引处的元素
                self.swap(index, i)
                # 递归生成剩余元素的排列
                self.generate_permutations(index + 1, result)
                # 撤销交换以回溯并探索其他可能性
                self.swap(index, i)

    def swap(self, i, j):
        # 交换数组值
        temp = self.item[i]
        self.item[i] = self.item[j]
        self.item[j] = temp