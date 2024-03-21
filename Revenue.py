from json import tool
"""
 这个函数是计算agentA的收益值，如果没出现在bundle 中则值为0
"""

class Revenue:
    @staticmethod
    def compute_revenue(agent_a, agent_b, agent_c, res, bundle,vector):
        tool.sum = 0.0
        for i in range(len(agent_a)):

            if (agent_a[i] == agent_b[i] and agent_a[i] != agent_c[i]) or (
                    agent_a[i] == agent_c[i] and agent_a[i] != agent_b[i]):
                if agent_a[i] in bundle:
                    res[i] = 0.5
                    vector[1] = vector[1] + 1
                    tool.sum += res[i]
                    continue
                else:
                    res[i] = 0
                    continue
            if agent_a[i] == agent_c[i] and agent_a[i] == agent_b[i]:
                if agent_a[i] in bundle:
                    res[i] = 0.33
                    vector[2] = vector[2] + 1
                    tool.sum += res[i]
                    continue
                else:
                    res[i] = 0
                    continue
            if agent_a[i] != agent_b[i] and agent_a[i] != agent_c[i]:
                if agent_a[i] in bundle:
                    res[i] = 1
                    vector[0] = vector[0] + 1
                    tool.sum += res[i]
                    continue
                else:
                    res[i] = 0
                    continue

        return round(tool.sum, 2)
