from thingsFirstPlace import thingsFirstPlace

if __name__ == '__main__':
    num = 11
    bundle = [2, 11, 4, 9, 5, 8]
    Agent_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    Agent_c = [10, 11, 2, 9, 8, 4, 1, 7, 5, 6, 3]
    f_p = []
    first_place = thingsFirstPlace.set_color(Agent_b, Agent_c, num, f_p)
    print(f_p)