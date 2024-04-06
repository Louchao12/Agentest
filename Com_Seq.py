

from CompetitiveSequence import CompetitiveSequence

if __name__ == '__main__':
    agent_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    agent_c = [16, 14, 15, 13, 4, 6, 3, 7, 10, 9, 5, 8, 1, 2, 12, 11]
    num = 16
    res1 = [0]*num
    res2 = [0]*num
    CompetitiveSequence.compete(agent_b, agent_c, res1, res2, num)
    res1=[elem for elem in res1 if elem != 0]
    res2=[elem for elem in res2 if elem != 0]
    print(res1)
    print(res2)