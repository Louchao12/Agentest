class thingsFirstPlace:


    @staticmethod
    def set_color(Agent_B, Agent_C, num, first_place):
        _set = set(range(1, num + 1))

        i, j = 0, 0
        while i < len(Agent_B) or j < len(Agent_C):
            if i < len(Agent_B) and j < len(Agent_C) and _set.__contains__(Agent_B[i]) and _set.__contains__(Agent_C[j]) and Agent_B[i] == Agent_C[j]:
                first_place[Agent_B[i]] = i + 1
                _set.remove(Agent_B[i])

            if i < len(Agent_B) and j < len(Agent_C) and _set.__contains__(Agent_B[i]) and _set.__contains__(Agent_C[j]) and Agent_B[i] != Agent_C[j]:
                first_place[Agent_B[i]] = i + 1
                first_place[Agent_C[j]] = i + 1
                _set.remove(Agent_B[i])
                _set.remove(Agent_C[j])

            if i < len(Agent_B) and _set.__contains__(Agent_B[i]) and not _set.__contains__(Agent_C[j]):
                first_place[Agent_B[i]] = i + 1
                _set.remove(Agent_B[i])

            if j < len(Agent_C) and _set.__contains__(Agent_C[j]) and not _set.__contains__(Agent_B[i]):
                first_place[Agent_C[j]] = i + 1
                _set.remove(Agent_C[i])

            i += 1
            j += 1



