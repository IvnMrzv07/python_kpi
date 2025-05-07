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


def find_el_by_pos_with_pivot(lst, pivot, el_pos):
    left_l = []
    right_l = []

    for el in lst:
        if el <= pivot:
            left_l.append(el)
        elif el > pivot:
            right_l.append(el)
    if len(left_l) + len(right_l) == len(lst):
        left_l.pop(left_l.index(pivot))

    pivot_pos = len(left_l)
    devitation = abs(el_pos - pivot_pos)

    if devitation == 0:
        res = pivot
    elif len(left_l) > len(right_l):
        res = iter_buble(left_l, devitation, 1)
    elif len(left_l) < len(right_l):
        res = iter_buble(right_l, devitation, -1)
    else:
        res = pivot

    return res


def find_median(lst):
    pivot = pivot_for_median(lst)
    if (len(lst)/2 - len(lst)//2) == 0:
        el_pos = len(lst)//2
        median = find_el_by_pos_with_pivot(lst, pivot, el_pos)
    else:
        el_pos = len(lst)//2
        r_m = find_el_by_pos_with_pivot(lst, pivot, el_pos)
        el_pos = len(lst)//2-1
        l_m = find_el_by_pos_with_pivot(lst, pivot, el_pos)
        median = (r_m + l_m)/2
    return median


while True:
    u = input("1 - start\n0 - exit\n>>>")
    if u == "1":
        start = time.time()
        len_of_l = int(input("Enter length of list: "))
        l = []

        for i in range(len_of_l):
            l.append(randint(0, 100))

        median = find_median(l)

        # print("Random list:")
        # for el in l:
        #     print(el, end=" ")
        # print("\n")
        print(f"My median - {median}\n")

        l.sort()
        #print("Sorted list: ")
        # for el in l:
        #     print(el, end=" ")
        # print("\n")
        print(f"True median - {l[len(l)//2]}\n")

        end = time.time()-start
        print(f"Runtime = {end}\n")

    elif u == "0":
        print("idi nah")
        exit()
    else:
        print("sho vysral?")


