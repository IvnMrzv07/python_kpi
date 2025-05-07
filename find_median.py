from random import randint
import time

def timer(function):
    def wrapped(*args):
        start_time = time.time()
        res = function(*args)
        print(f"Runtime: ",time.time() - start_time)
        return res
    return wrapped

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

def select(lst, k):
    left_l = []
    right_l = []
    pivots_l = []
    pivot = pivot_for_median(lst)
    for el in lst:
        if el < pivot:
            left_l.append(el)
        elif el > pivot:
            right_l.append(el)
        else:
            pivots_l.append(el)

    if k < len(left_l): # lst[k] < pivot
        return select(left_l, k)
    elif k < (len(left_l)+len(pivots_l)): # lst[k] == pivot
        return pivot
    else: # lst[k] > pivot
        return select(right_l, k - len(left_l) - len(pivots_l))

def median_with_select(lst):
    if len(lst)//2 == len(lst)/2:
        l_m = select(lst, len(lst)//2-1)
        r_m = select(lst, len(lst)//2)
        median = (l_m+r_m)/2
        return median
    else:
        median = select(lst, len(lst)//2)
        return median

while True:
    u = input("1 - start\n0 - exit\n>>>")
    if u == "1":
        len_of_l = int(input("Enter length of list: "))
        l = []

        for i in range(len_of_l):
            l.append(randint(0, 1000000))

        # print("Random list:")
        # for el in l:
        #     print(el, end=" ")
        # print("\n")

        median2 = median_with_select(l)
        print(f"My recursive median: {median2}\n")

        l.sort()

        # print("Sorted list: ")
        # for el in l:
        #     print(el, end=" ")
        # print("\n")

        if len_of_l//2 == len_of_l/2:
            true_median = (l[len(l)//2 -1] + l[len(l)//2])/2
        else:
            true_median = l[len(l)//2]
        print(f"True median: {true_median}\n")

    elif u == "0":
        print("idi nah")
        exit()
    else:
        print("sho vysral?")


