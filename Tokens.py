"""
    初始化tokens，给其他函数用，第一位存储物品个数，物品按照序号初始化从1-n
"""
class Tokens:
    def __init__(self):
        self.num = 0

    def get_num(self):
        return self.num

    def set_num(self, num):
        self.num = num

    def taken(self, num):
        ans = [0] * (num + 1)
        ans[0] = num
        for i in range(1, len(ans)):
            ans[i] = 1
        return ans