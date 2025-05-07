from random import randint
import time

def timer(function): # функція - декоратор, для виведення часу роботи програми
    def wrapped(*args):
        start_time = time.time()
        res = function(*args)
        print(f"Runtime: ",time.time() - start_time)
        return res
    return wrapped

def pivot_for_median(lst): #знаходження вдалого опорного елемента, для того щоб максимізувати швидкість зменшення задачі(видкидати якомога більше елементів)
    l_medians = []

    for i in range(0, len(lst), 5):
        chunk = lst [i:i + 5] # принцип median of medians, розбиття на групки <=5 елементів
        chunk.sort() # сортування груп, має певний сталий час

        if len(chunk) % 2 == 0: # логіка для залишкової групки, якщо вхідний список !/5(парне/не парне число елементів в залишковій групі)
            l_medians.append((chunk[len(chunk)//2] + chunk[len(chunk)//2-1])/2)
        else:
            l_medians.append(chunk[len(chunk) // 2])

    if len(l_medians) <= 5: # логіка рекурсивного зменшення задачі, бо при великих n сортувати приблизно n/5 елементів, всеодно дуже довго
        l_medians.sort()
        if len(l_medians) % 2 == 0: #парне/непарне
            pivot = (l_medians[len(l_medians) // 2] + l_medians[len(l_medians) // 2 - 1])/2
        else:
            pivot = l_medians[len(l_medians) // 2]
        return pivot
    else:
        return pivot_for_median(l_medians)

def select(lst, k):  # власне використання pivot, логіка відкидання тої частини списку де точно немає медіани, та рекурсивне заглиблення
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

    if k < len(left_l): # lst[k] < pivot тобто якщо медіана лежить десь в лівому списку, рекурсивно переходимо туди
        return select(left_l, k)
    elif k > len(left_l) and k < len(left_l) + len(pivots_l): # lst[k] > pivot - якщо медіана в правому списку, переходимо туди, і зменшуємо наш номер к(умовно відрізаємо хвіст)
        return select(right_l, k - len(left_l) - len(pivots_l))
    else: # lst[k] == pivot ну і умова виходу з рекурсії, якщо медіана не в лівому і не в правому списку, то вона == pivot, ми знайшли її
        return pivot

@timer
def median_with_select(lst): # логіка знаходження самої медіани, тобто збираємо все до купи
    if len(lst) % 2 == 0: # вже знайома парність/непарність, яка впливає на те як саме шукати медіану
        l_m = select(lst, len(lst)//2-1) # "ліва медіана"
        r_m = select(lst, len(lst)//2) # "права медіана"
        median = (l_m+r_m)/2 # ну і сам результат, середнє арифметичне з цих двох
        return median
    else:
        median = select(lst, len(lst)//2) # тут все зрозуміло
        return median

if __name__ == '__main__': # (використовувалось в процесі написання, для зручності імпорту функцій, для перевірки)
    while True:
        u = input("1 - start\n0 - exit\n>>>")

        if u == "1":
            len_of_l = int(input("Enter length of list: "))
            l = []

            for i in range(len_of_l): #генерація списку з рандомними числами
                l.append(randint(0, 1000000))

            # в коментах виведення списків, якщо потрібно

            # print("Random list:")
            # for el in l:
            #     print(el, end=" ")
            # print("\n")

            median = median_with_select(l) # знаходження медіани для згенерованого списку
            print(f"My median with selection: {median}\n")

            l.sort() # сортування в лоб, не стосується алгоритму, дано просто для перевірки правильності

            # print("Sorted list: ")
            # for el in l:
            #     print(el, end=" ")
            # print("\n")

            if len_of_l % 2  == 0: # знаходження медіани в лоб, по вже відсортованому списку
                true_median = (l[len(l)//2 -1] + l[len(l)//2])/2
            else:
                true_median = l[len(l)//2]

            print(f"True median: {true_median}\n")

        elif u == "0": # просто інтерфейс взаємодії з програмою
            print("exiting...")
            exit()
        else:
            print("wrong input!")


