from Tokens import Tokens
# 这是计算两个人竞争的代码块，输出两个人竞争后的竞争序列

class CompetitiveSequence:
    def compete(self, person1, person2, result1, result2, num):
        taken = Tokens().taken(num)

        i = j = 0
        while i < num and j < num:
            if taken[0] <= 0:
                break

            while taken[0] > 0 and i < num and j < num:
                if taken[0] > 0 and j < num and i < num and taken[person1[i]] * taken[person2[j]] == 0:
                    while i < num and taken[person1[i]] == 0 and taken[0] > 0:
                        i += 1
                    while j < num and taken[person2[j]] == 0 and taken[0] > 0:
                        j += 1

                    if j < num and i < num and person1[i] == person2[j] and taken[0] > 0:
                        # 如果物品相同，则都获得
                        result1[i] = person1[i]
                        result2[j] = person2[j]
                        taken[person1[i]] = 0
                        taken[0] -= 1
                        break

                    if j < num and i < num and person1[i] != person2[j] and taken[0] > 0:
                        # 如果物品不相同，则分别获得
                        result1[i] = person1[i]
                        result2[j] = person2[j]
                        taken[person1[i]] = 0
                        taken[person2[j]] = 0
                        taken[0] -= 2
                        break

                if j < num and i < num and taken[person1[i]] * taken[person2[j]] != 0 and person1[i] != person2[j] and \
                        taken[0] > 0:
                    # 如果物品不相同，则分别获得
                    result1[i] = person1[i]
                    result2[j] = person2[j]
                    taken[person1[i]] = 0
                    taken[person2[j]] = 0
                    taken[0] -= 2
                    break

                if j < num and i < num and taken[person1[i]] * taken[person2[j]] != 0 and person1[i] == person2[j] and \
                        taken[0] > 0:
                    # 如果物品相同，则都获得
                    result1[i] = person1[i]
                    result2[j] = person2[j]
                    taken[person1[i]] = 0
                    taken[0] -= 1
                    break
