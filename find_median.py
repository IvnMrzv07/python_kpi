from random import randint
import time

def pivot_for_median(lst):
    l = lst.copy()
    l_medians = []
    l_help = [0]*5
    len_of_l = len(l)

    if (len_of_l - len_of_l//5*5) != 0:
        for i in range((len_of_l//5*5+5)-len_of_l):
            l.append(0)

    for i in range(0, len(l), 5):
        for j in range(5):
            l_help[j] = l[i + j]
        l_help.sort()
        l_medians.append(l_help[2])

    l_medians.sort()
    pivot = l_medians[len(l_medians)//2]

    return pivot

def iter_buble(lst, num_of_els, max_min):
    res_l = []
    l = lst.copy()
    if max_min == 1:
        for i in range(num_of_els):
            max_val = l[0]
            for el in l:
                if el > max_val:
                    max_val = el

            res_l.append(max_val)
            l.pop(l.index(max_val))
    elif max_min == -1:
        for i in range(num_of_els):
            min_val = l[0]
            for el in l:
                if el < min_val:
                    min_val = el

            res_l.append(min_val)
            l.pop(l.index(min_val))
    else:
        print("wrong max_min, it can be only 1 or -1")
        return 0

    return res_l[-1]

while True:
    u = input("1 - start\n0 - exit\n>>>")
    if u == "1":
        start = time.time()
        len_of_l = int(input("Enter length of list: "))
        l = []
        left_l = []
        right_l = []

        # print("\nRandom list: ")
        for i in range(len_of_l):
            l.append(randint(0, 100))
            # print(l[i], end=" ")

        pivot = pivot_for_median(l)

        for el in l:
            if el <= pivot:
                left_l.append(el)
            if el > pivot:
                right_l.append(el)
        if len(left_l)+len(right_l)+1 != len_of_l:
            left_l.pop(left_l.index(pivot))

        res = 0
        pivot_pos = len(left_l)
        devitation = abs(len_of_l//2 - pivot_pos) ## +1

        # if devitation == 0:
        #     median = pivot
        if len(left_l) > len(right_l):
            median = iter_buble(left_l, devitation, 1)
        elif len(left_l) < len(right_l):
            median = iter_buble(right_l, devitation, -1)
        else:
            median = pivot

        print(f"\nMy median = {median}")

        # print(f"{left_l} {pivot} {right_l}")
        # print(f"len of left = {len(left_l)} len of right = {len(right_l)}")
        #
        # print("\nSorted list: ")
        l.sort()
        # for i in range(len(l)):
        #     print(l[i], end=" ")
        print(f"\nTrue median - {l[len(l)//2]}\n")
        end = time.time()-start
        print(end)

    elif u == "0":
        print("idi nah")
        exit()
    else:
        print("sho vysral?")

