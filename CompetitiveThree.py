# -*- coding: utf-8 -*-
from Tokens import Tokens


# 这是三个人竞争的代码块，返回三个人竞争的拿取序列

class CompetitiveThree:
    def __init__(self, num):
        num = num

    # (碰撞序列，agent_b偏好，agent_c偏好，b序列，c序列，a序列，物品数)
    def competitive_n(self, sequences, person1, person2, result1, result2, boss, num):
        taken = Tokens().taken(num)

        i = j = k = 0
        while i < num and j < num and k < num and sequences[k] != 0:
            if taken[0] <= 0:
                break
            # 剩余物品 > 0,并且index < num
            while taken[0] > 0 and i < num and j < num and k < num and sequences[k] != 0:
                # 如果第i个物品被拿取了，就报下一个
                if j < num and i < num and k < num and taken[person1[i]] * taken[person2[j]] * taken[
                    sequences[k]] == 0 and taken[0] > 0:

                    while i < num and taken[person1[i]] == 0 and taken[0] > 0:
                        i = i + 1
                    while j < num and taken[person2[j]] == 0 and taken[0] > 0:
                        j = j + 1
                    while k < num and taken[sequences[k]] == 0 and taken[0] > 0:
                        k = k + 1

                    # index < num && 三人申报物品相等，且剩余物品 > 0
                    if j < num and i < num and k < num and person1[i] == person2[j] == sequences[k] and taken[0] > 0:
                        result1[i] = person1[i]
                        result2[j] = person2[j]
                        boss[k] = sequences[k]
                        taken[person1[i]] = 0
                        taken[0] -= 1
                        break

                    if j < num and i < num and k < num and person1[i] != person2[j] and person1[i] != \
                            sequences[k] and person2[j] != sequences[k] and taken[0] > 0:
                        result1[i] = person1[i]
                        result2[j] = person2[j]
                        boss[k] = sequences[k]
                        taken[person1[i]] = 0
                        taken[person2[j]] = 0
                        taken[sequences[k]] = 0
                        taken[0] -= 3
                        break

                    if j < num and i < num and k < num and person1[i] == person2[j] and person1[i] != \
                            sequences[k] and taken[0] > 0:
                        result2[j] = person2[j]
                        result1[i] = person1[i]
                        boss[k] = sequences[k]
                        taken[person2[j]] = 0
                        taken[sequences[k]] = 0
                        taken[0] -= 2
                        break

                    if j < num and i < num and k < num and person1[i] != person2[j] and person1[i] == \
                            sequences[k] and taken[0] > 0:
                        result1[i] = person1[i]
                        result2[j] = person2[j]
                        boss[k] = sequences[k]
                        taken[person1[i]] = 0
                        taken[person2[j]] = 0
                        taken[0] -= 2
                        break

                    if j < num and i < num and k < num and person1[i] != person2[j] and person2[j] == \
                            sequences[k] and taken[0] > 0:
                        result1[i] = person1[i]
                        result2[j] = person2[j]
                        boss[k] = sequences[k]
                        taken[person1[i]] = 0
                        taken[person2[j]] = 0
                        taken[0] -= 2
                        break

                # 如果申报物品全都还在，并且三个人报的物品全不相同
                if j < num and i < num and k < num and taken[person1[i]] * taken[person2[j]] * taken[
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

                if j < num and i < num and k < num and taken[person1[i]] * taken[person2[j]] != 0 and \
                        person1[i] == person2[j] and person1[i] == sequences[k] and person2[j] == sequences[k] and \
                        taken[0] > 0:
                    result1[i] = person1[i]
                    result2[j] = person2[j]
                    boss[k] = sequences[k]
                    taken[person1[i]] = 0
                    taken[0] -= 1
                    break

                if j < num and i < num and k < num and person1[i] == person2[j] and person1[i] != \
                        sequences[k] and taken[0] > 0:
                    result2[j] = person2[j]
                    result1[i] = person1[i]
                    boss[k] = sequences[k]
                    taken[person2[j]] = 0
                    taken[sequences[k]] = 0
                    taken[0] -= 2
                    break

                if j < num and i < num and k < num and person1[i] != person2[j] and person1[i] == \
                        sequences[k] and taken[0] > 0:
                    result1[i] = person1[i]
                    result2[j] = person2[j]
                    boss[k] = sequences[k]
                    taken[person1[i]] = 0
                    taken[person2[j]] = 0
                    taken[0] -= 2
                    break

                if j < num and i < num and k < num and person1[i] != person2[j] and person2[j] == \
                        sequences[k] and taken[0] > 0:
                    result1[i] = person1[i]
                    result2[j] = person2[j]
                    boss[k] = sequences[k]
                    taken[person1[i]] = 0
                    taken[person2[j]] = 0
                    taken[0] -= 2
                    break


