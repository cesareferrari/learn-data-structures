"""
initialize swap counter
initialize last index of unsorted sublist to last index of list

while swap count is true (more than zero)
    set swap count to zero

    for all the numbers in array
        if the first number is bigger than the second number 
            swap them
            increment swap count

    decrement the last unsorted index

return list
"""

def bubble_sort(list):
    swap = 1
    last_unsorted_idx = len(list) - 1

    while swap:
        swap = 0

        for i in range(last_unsorted_idx):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                swap += 1

        last_unsorted_idx -= 1

    return list



print(bubble_sort([65, 55, 45, 35, 25, 15, 10]))
