
from Tokens import Tokens


# 这是三个人竞争的代码块，返回三个人竞争的拿取序列

class CompetitiveThree:
    def __init__(self, num):
        self.num = num

    # (碰撞序列，agent_b偏好，agent_c偏好，b序列，c序列，a序列，物品数)
    def competitive_n(self, sequences, person1, person2, result1, result2, boss, num):
        taken = Tokens().taken(num)

        i = j = k = 0
        while i < self.num and j < self.num and k < self.num and sequences[k] != 0:
            if taken[0] <= 0:
                break

            while taken[0] > 0 and i < self.num and j < self.num and k < self.num and sequences[k] != 0:
                if j < self.num and i < self.num and k < self.num and taken[person1[i]] * taken[person2[j]] * taken[
                    sequences[k]] == 0 and taken[0] > 0:

                    i = self.find_next_nonzero(taken, person1, i)
                    j = self.find_next_nonzero(taken, person2, j)
                    k = self.find_next_nonzero(taken, sequences, k)

                    if j < self.num and i < self.num and k < self.num and person1[i] == person2[j] and person1[i] == \
                            sequences[k] and person2[j] == sequences[k] and taken[0] > 0:
                        result1[i] = person1[i]
                        result2[j] = person2[j]
                        boss[k] = sequences[k]
                        taken[person1[i]] = 0
                        taken[0] -= 1
                        break

                    if j < self.num and i < self.num and k < self.num and person1[i] != person2[j] and person1[i] != \
                            sequences[k] and person2[j] != sequences[k] and taken[0] > 0:
                        result1[i] = person1[i]
                        result2[j] = person2[j]
                        boss[k] = sequences[k]
                        taken[person1[i]] = 0
                        taken[person2[j]] = 0
                        taken[sequences[k]] = 0
                        taken[0] -= 3
                        break

                    if j < self.num and i < self.num and k < self.num and person1[i] == person2[j] and person1[i] != \
                            sequences[k] and taken[0] > 0:
                        result2[j] = person2[j]
                        result1[i] = person1[i]
                        boss[k] = sequences[k]
                        taken[person2[j]] = 0
                        taken[sequences[k]] = 0
                        taken[0] -= 2
                        break

                    if j < self.num and i < self.num and k < self.num and person1[i] != person2[j] and person1[i] == \
                            sequences[k] and taken[0] > 0:
                        result1[i] = person1[i]
                        result2[j] = person2[j]
                        boss[k] = sequences[k]
                        taken[person1[i]] = 0
                        taken[person2[j]] = 0
                        taken[0] -= 2
                        break

                    if j < self.num and i < self.num and k < self.num and person1[i] != person2[j] and person2[j] == \
                            sequences[k] and taken[0] > 0:
                        result1[i] = person1[i]
                        result2[j] = person2[j]
                        boss[k] = sequences[k]
                        taken[person1[i]] = 0
                        taken[person2[j]] = 0
                        taken[0] -= 2
                        break

                if j < self.num and i < self.num and k < self.num and taken[person1[i]] * taken[person2[j]] * taken[
                    sequences[k]] != 0 and person1[i] != person2[j] and person1[i] != sequences[k] and person2[j] != \
                        sequences[k] and taken[0] > 0:
                    result1[i] = person1[i]
                    result2[j] = person2[j]
                    boss[k] = sequences[k]
                    taken[person1[i]] = 0
                    taken[person2[j]] = 0
                    taken[sequences[k]] = 0
                    taken[0] -= 3
                    break

                if j < self.num and i < self.num and k < self.num and taken[person1[i]] * taken[person2[j]] != 0 and \
                        person1[i] == person2[j] and person1[i] == sequences[k] and person2[j] == sequences[k] and \
                        taken[0] > 0:
                    result1[i] = person1[i]
                    result2[j] = person2[j]
                    boss[k] = sequences[k]
                    taken[person1[i]] = 0
                    taken[0] -= 1
                    break

                if j < self.num and i < self.num and k < self.num and person1[i] == person2[j] and person1[i] != \
                        sequences[k] and taken[0] > 0:
                    result2[j] = person2[j]
                    result1[i] = person1[i]
                    boss[k] = sequences[k]
                    taken[person2[j]] = 0
                    taken[sequences[k]] = 0
                    taken[0] -= 2
                    break

                if j < self.num and i < self.num and k < self.num and person1[i] != person2[j] and person1[i] == \
                        sequences[k] and taken[0] > 0:
                    result1[i] = person1[i]
                    result2[j] = person2[j]
                    boss[k] = sequences[k]
                    taken[person1[i]] = 0
                    taken[person2[j]] = 0
                    taken[0] -= 2
                    break

                if j < self.num and i < self.num and k < self.num and person1[i] != person2[j] and person2[j] == \
                        sequences[k] and taken[0] > 0:
                    result1[i] = person1[i]
                    result2[j] = person2[j]
                    boss[k] = sequences[k]
                    taken[person1[i]] = 0
                    taken[person2[j]] = 0
                    taken[0] -= 2
                    break

    def find_next_nonzero(self, taken, person, index):
        while index < self.num and taken[person[index]] == 0 and taken[0] > 0:
            index += 1
        return index
