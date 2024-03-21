def generate_nonempty_power_set(input_set):
    # �������м���
    # if not input_set:
    #     return []  # Return an empty list if the input set is empty
    #
    # power_set = []
    # input_list = list(input_set)  # Convert the set to a list
    # n = len(input_list)
    #
    # for i in range(1, 1 << n):
    #     subset = [input_list[j] for j in range(n) if (i & (1 << j)) > 0]
    #     power_set.append(subset)
    #
    # return power_set

    # ��������ӵ��һ��Ԫ�ص��Ӽ�
    if not input_set:
        return []  # Return an empty list if the input set is empty

    power_set = []
    input_list = list(input_set)  # Convert the set to a list
    n = len(input_list)
    min_subset_size = (n + 1) // 2

    for i in range(1, 1 << n):
        subset = [input_list[j] for j in range(n) if (i & (1 << j)) > 0]
        if len(subset) >= min_subset_size:
            power_set.append(subset)

    return power_set