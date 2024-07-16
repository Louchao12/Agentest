import ast

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
    for i in range(len(bundle)):
        o = []
        index_b = Agent_b.index(bundle[i])
        index_c = Agent_c.index(bundle[i])
        gap = abs(index_b - index_c)
        o.append(bundle[i])
        o.append(gap)
        site.append(o)
    print(site)

    i = j = 0
    while tokens:
        while i < num and j < num:
            if Agent_b[i] in tokens and Agent_c[j] in tokens:
                o_b = Agent_b[i]
                o_c = Agent_c[j]
                tokens.discard(Agent_b[i])
                tokens.discard(Agent_c[j])
                print(o_b, o_c)
                i = j = 0
                break
            if Agent_b[i] not in tokens:
                i = i + 1
            if Agent_c[j] not in tokens:
                j = j + 1
        if o_b in bundle and o_c in bundle:
            N = N + 1
            if o_b != o_c:
                if len(stack) > 0:
                    b_site = next((index for index, sublist in enumerate(site) if sublist[0] == o_b), None)
                    c_site = next((index for index, sublist in enumerate(site) if sublist[0] == o_c), None)
                    if site[b_site][1] >= site[c_site][1]:
                        o_a.append(o_b)
                        tokens.add(o_c)
                        stack.pop()
                        continue
                    else:
                        o_a.append(o_b)
                        tokens.add(o_c)
                        stack.pop()
                        continue
                else:
                    o = [o_b, o_c, N]
                    stack.append(o)
                    continue
            if o_b == o_c:
                if len(stack) > 0:
                    o_a.append(o_b)
                    stack.pop()
                    continue
                else:
                    o = [o_b, o_c, N]
                    stack.append(o)
                    continue
        if o_b in bundle:
            N = N + 1
            if len(stack) > 0:
                o_a.append(o_b)
                tokens.add(o_c)
                stack.pop()
                continue
            else:
                o = [o_b, o_c, N]
                stack.append(o)
                continue
        if o_c in bundle:
            N = N + 1
            if len(stack) > 0:
                o_a.append(o_c)
                tokens.add(o_b)
                stack.pop()
                continue
            else:
                o = [o_b, o_c, N]
                stack.append(o)
                continue
        if o_b not in bundle and o_c not in bundle:
            o = [o_b, o_c, -1]
            stack.append(o)
    if stack:
        o = stack[0]
        if o[2] != -1:
            if o[0] in bundle:
                o_a.insert(o[2] - 1, o[0])
            else:
                o_a.insert(o[2] - 1, o[1])
        else:
            return o_a
    return o_a


if __name__ == '__main__':
    num = 5
    bundle = [1,2,3,4]
    Agent_b = [4,1,2,3]
    Agent_c = [1,2,3,4]
    o_a=OA(num, bundle, Agent_b, Agent_c)
    print(o_a)
