import Algorithm
from CompetitiveThree import CompetitiveThree
from Revenue import Revenue
import Alg


class writeFile2:

    def write(agent_b, agent_c, bundle, num):
        separator = "=" * 80
        o_a = Algorithm.OA(num, bundle, agent_b, agent_c)
        for i in range(num - len(bundle)):
            o_a.append(0)
        competition_three = CompetitiveThree(num)
        competition_a = [0] * num
        competition_b = [0] * num
        competition_c = [0] * num
        competition_three.competitive_n(o_a, agent_b, agent_c, competition_b, competition_c,
                                        competition_a, num)
        # 生成Agent A,B,C 的获得物品集

        competition_a = [elem for elem in competition_a if elem != 0]
        competition_b = [elem for elem in competition_b if elem != 0]
        competition_c = [elem for elem in competition_c if elem != 0]

        data_a = competition_a
        data_b = competition_b
        data_c = competition_c
        revenue = Revenue()
        res = [0] * len(data_a)
        vector = 0
        E, vector = revenue.compute_revenue(data_a, data_b, data_c, res, bundle, vector)
        with open('E:\\pydemo\\Agent\\R.text', 'a') as file_agent_revenue, \
                open('temp2.txt', 'w') as file_temp:
            file_temp.write('bundle:' + str(bundle) + 'Bs:' + str(agent_b) + 'Cs:' + str(agent_c) + 'A:' + str(
                    data_a) + 'B:' + str(data_b) + 'C:' + str(data_c) + "收益为： " + str(E) + " 收益向量为：" + str(
                    res) + "收益矩阵为：" + str(vector) + '\n')
            file_agent_revenue.write(
                'bundle:' + str(bundle) + 'Bs:' + str(agent_b) + 'Cs:' + str(agent_c) + 'A:' + str(
                    data_a) + 'B:' + str(data_b) + 'C:' + str(data_c) + "收益为： " + str(E) + " 收益向量为：" + str(
                    res) + "收益矩阵为：" + str(vector) + '\n')
            file_agent_revenue.write(separator + '\n')
        return E
