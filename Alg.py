import ast
# -*- coding: utf-8 -*-
from CompetitiveThree import CompetitiveThree
from Revenue import Revenue
from thingsFirstPlace import thingsFirstPlace

'''
bundle:{1, 2, 4, 5, 6}Bs:[1, 2, 3, 4, 5, 6]Cs:[3, 2, 6, 5, 4, 1]A:[6, 5, 4]B:[1, 2, 4]C:[3, 2, 4] 收益为： 2.33 收益向量为：[1, 1, 0.33]收益矩阵为：201
bundle:{1, 2, 4, 5, 6}Bs:[1, 2, 3, 4, 5, 6]Cs:[3, 2, 6, 5, 4, 1]A:[5, 4, 6]B:[1, 2, 6]C:[3, 2, 6] 收益为： 2.33 收益向量为：[1, 1, 0.33]收益矩阵为：201
bundle:{1, 2, 4, 5, 6}Bs:[1, 2, 3, 4, 5, 6]Cs:[3, 2, 6, 5, 4, 1]A:[4, 5, 6]B:[1, 2, 6]C:[3, 2, 6] 收益为： 2.33 收益向量为：[1, 1, 0.33]收益矩阵为：201
bundle:{1, 2, 4, 5, 6}Bs:[1, 2, 3, 4, 5, 6]Cs:[3, 2, 6, 5, 4, 1]A:[6, 4, 5]B:[1, 2, 5]C:[3, 2, 5] 收益为： 2.33 收益向量为：[1, 1, 0.33]收益矩阵为：201
bundle:{1, 2, 4, 5, 6}Bs:[1, 2, 3, 4, 5, 6]Cs:[3, 2, 6, 5, 4, 1]A:[5, 6, 4]B:[1, 2, 4]C:[3, 2, 4] 收益为： 2.33 收益向量为：[1, 1, 0.33]收益矩阵为：201
bundle:{1, 2, 4, 5, 6}Bs:[1, 2, 3, 4, 5, 6]Cs:[3, 2, 6, 5, 4, 1]A:[4, 6, 5]B:[1, 2, 5]C:[3, 2, 5] 收益为： 2.33 收益向量为：[1, 1, 0.33]收益矩阵为：201
bundle:{1, 2, 4, 5, 6}Bs:[1, 2, 3, 4, 5, 6]Cs:[2, 1, 5, 3, 4, 6]A:[5, 6, 4]B:[1, 3, 4]C:[2, 3, 4] 收益为： 2.33 收益向量为：[1, 1, 0.33]收益矩阵为：201
bundle:{1, 2, 4, 5, 6}Bs:[1, 2, 3, 4, 5, 6]Cs:[2, 1, 5, 3, 4, 6]A:[5, 4, 6]B:[1, 3, 6]C:[2, 3, 6] 收益为： 2.33 收益向量为：[1, 1, 0.33]收益矩阵为：201
bundle:{1, 2, 4, 5, 6}Bs:[1, 2, 3, 4, 5, 6]Cs:[3, 1, 5, 2, 6, 4]A:[5, 4, 6]B:[1, 2, 6]C:[3, 2, 6] 收益为： 2.33 收益向量为：[1, 1, 0.33]收益矩阵为：201
bundle:{1, 2, 4, 5, 6}Bs:[1, 2, 3, 4, 5, 6]Cs:[3, 1, 5, 2, 6, 4]A:[5, 6, 4]B:[1, 2, 4]C:[3, 2, 4] 收益为： 2.33 收益向量为：[1, 1, 0.33]收益矩阵为：201
bundle:{1, 2, 4, 5, 6}Bs:[1, 2, 3, 4, 5, 6]Cs:[5, 3, 1, 6, 4, 2]A:[2, 4, 6]B:[1, 3, 6]C:[5, 3, 6] 收益为： 2.33 收益向量为：[1, 1, 0.33]收益矩阵为：201
bundle:{1, 2, 4, 5, 6}Bs:[1, 2, 3, 4, 5, 6]Cs:[5, 3, 1, 6, 4, 2]A:[2, 6, 4]B:[1, 3, 4]C:[5, 3, 4] 收益为： 2.33 收益向量为：[1, 1, 0.33]收益矩阵为：201
bundle:{1, 2, 4, 5, 6}Bs:[1, 2, 3, 4, 5, 6]Cs:[6, 3, 1, 2, 4, 5]A:[2, 5, 4]B:[1, 3, 4]C:[6, 3, 4] 收益为： 2.33 收益向量为：[1, 1, 0.33]收益矩阵为：201
bundle:{1, 2, 4, 5, 6}Bs:[1, 2, 3, 4, 5, 6]Cs:[6, 3, 1, 2, 4, 5]A:[2, 4, 5]B:[1, 3, 5]C:[6, 3, 5] 收益为： 2.33 收益向量为：[1, 1, 0.33]收益矩阵为：201
bundle:{1, 2, 4, 5, 6}Bs:[1, 2, 3, 4, 5, 6]Cs:[3, 4, 2, 1, 6, 5]A:[2, 5, 6]B:[1, 4, 6]C:[3, 4, 6] 收益为： 2.33 收益向量为：[1, 1, 0.33]收益矩阵为：201
bundle:{1, 2, 4, 5, 6}Bs:[1, 2, 3, 4, 5, 6]Cs:[3, 4, 2, 1, 6, 5]A:[2, 6, 5]B:[1, 4, 5]C:[3, 4, 5] 收益为： 2.33 收益向量为：[1, 1, 0.33]收益矩阵为：201
bundle:{1, 2, 4, 5, 6}Bs:[1, 2, 3, 4, 5, 6]Cs:[3, 4, 2, 1, 6, 5]A:[4, 5, 6]B:[1, 2, 6]C:[3, 2, 6] 收益为： 2.33 收益向量为：[1, 1, 0.33]收益矩阵为：201

'''


def OA(num, bundle, Agent_b, Agent_c):
    N = 0
    stack = []
    o_a = []
    site = []
    tokens = set(range(1, num + 1))
    print(tokens)

    i = j = 0
    while tokens:
        choose = []
        N = N + 1
        while i < num and j < num:
            # 确定b，c所选物品
            if Agent_b[i] in tokens and Agent_c[j] in tokens:
                o_b = Agent_b[i]
                o_c = Agent_c[j]
                if i + 1 < num and j + 1 < num:
                    o_b_link = Agent_b[i + 1]
                    o_c_link = Agent_c[j + 1]
                else:
                    o_b_link = None
                    o_c_link = None
                tokens.discard(Agent_b[i])
                tokens.discard(Agent_c[j])
                k = i + 1
                q = j + 1
                o_b_next = None
                o_c_next = None
                while k < num and q < num:
                    if Agent_b[k] in tokens and Agent_c[q] in tokens:
                        o_b_next = Agent_b[k]
                        o_c_next = Agent_c[q]

                        break
                    if Agent_b[k] not in tokens:
                        k = k + 1
                    if Agent_c[q] not in tokens:
                        q = q + 1

                i = j = 0
                break
            if Agent_b[i] not in tokens:
                i = i + 1
            if Agent_c[j] not in tokens:
                j = j + 1

            # 如果b，c报的都是目标物品
        if o_b in bundle and o_c in bundle:
            # 如果b，c报的物品不相同
            if o_b != o_c:
                # 栈中存在缓冲物品
                if len(stack) > 0:
                    # ob后的物品不为空
                    if o_b_next is not None:
                        # ob的下一个物品是目标物品
                        if o_b_next in bundle:
                            # oc的下一个物品不是目标物品
                            if o_c_next not in bundle:
                                choose = [o_b, N]
                                o_a.append(choose)
                                tokens.add(o_c)
                                stack.pop()
                                continue
                    if o_b == o_c_link:
                        choose = [o_b, N]
                        o_a.append(choose)
                        tokens.add(o_c)
                        stack.pop()
                        continue
                    if o_c == o_b_link:
                        choose = [o_c, N]
                        o_a.append(choose)
                        tokens.add(o_b)
                        stack.pop()
                        continue
                    else:
                        choose = [o_c, N]
                        o_a.append(choose)
                        tokens.add(o_b)
                        stack.pop()
                        continue
                else:
                    o = [o_b, o_c, N]
                    stack.append(o)
                    continue
            if o_b == o_c:
                o = [o_b, o_c, N]
                stack.append(o)
                continue
        # 如果b选择了目标物品
        if o_b in bundle:
            N = N + 1
            if len(stack) > 0:
                choose = [o_b, N]
                o_a.append(choose)
                tokens.add(o_c)
                stack.pop()
                continue
            else:
                o = [o_b, o_c, N]
                stack.append(o)
                continue
        # 如果c选择了目标物品
        if o_c in bundle:
            N = N + 1
            if len(stack) > 0:
                choose = [o_c, N]
                o_a.append(choose)
                tokens.add(o_b)
                stack.pop()
                continue
            else:
                o = [o_b, o_c, N]
                stack.append(o)
                continue
        # 如果都没选择目标物品
        if o_b not in bundle and o_c not in bundle:
            o = [o_b, o_c, -1]
            stack.append(o)
    same_thing = 0
    if len(stack) > 0:
        stack_temp=[]
        for i in range(len(stack)):
            o = stack[i]
            if o[2] == -1:
                continue
            if o[0] == o[1]:
                stack_temp.append(o)
                same_thing = same_thing + 1
            if o[0] != o[1]:
                stack_temp.append(o)
        if len(stack_temp) > 0:
            o = stack_temp[0]
            if o[0] == o[1]:
                same_thing = same_thing - 1
            same_thing = same_thing % 2
            oa_temp = switch(same_thing,stack_temp,bundle)
            o_a = o_a + oa_temp
            o_a.sort(key=lambda x: x[1])
            OA = []
            for i in range(len(o_a)):
                o = o_a[i]
                OA.append(o[0])
        else:
            o_a.sort(key=lambda x: x[1])
            OA = []
            for i in range(len(o_a)):
                o = o_a[i]
                OA.append(o[0])
    else:
        o_a.sort(key=lambda x: x[1])
        OA = []
        for i in range(len(o_a)):
            o = o_a[i]
            OA.append(o[0])
    return OA


def switch(case, stack, bundle):
    match case:
        case 0:
            o_a_temp = []
            o = stack[0]
            if o[0] in bundle:
                choose_1 = o[0]
            else:
                choose_1 = o[1]
            choose = [choose_1, o[2]]
            o_a_temp.append(choose)
            stack.remove(o)
            if len(stack) < 2:
                return o_a_temp
            else:
                for i in range(1,len(stack),2):
                    choose = [stack[i][0], stack[i][2]]
                    o_a_temp.append(choose)
            return o_a_temp
        case 1:
            o_a_temp = []
            for i in range(1, len(stack), 2):
                o = stack[i]
                if o[0] in bundle:
                    choose_1 = o[0]
                else:
                    choose_1 = o[1]
                choose = [choose_1, stack[i][2]]
                o_a_temp.append(choose)
            return o_a_temp


if __name__ == '__main__':
    num = 5
    bundle = [1, 2, 3]
    Agent_b = [1,2,3,4,5]
    Agent_c = [1,4,3,2,5]
    o_a = OA(num, bundle, Agent_b, Agent_c)
    print(o_a)
