
class findMaxVector:
    def findMaxVector(data):
        # 计算三个向量的数目
        vector_max = 0
        vector_mid = 0
        vector_min = 0
        for i in range(len(data)):
            if data[i] == 1:
                vector_max = vector_max + 1
            if data[i] == 0.5:
                vector_mid = vector_mid + 1
            if data[i] == 0.33:
                vector_min = vector_min + 1

        max_vector = []
        max_vector[0] = vector_max
        max_vector[1] = vector_mid
        max_vector[2] = vector_min
