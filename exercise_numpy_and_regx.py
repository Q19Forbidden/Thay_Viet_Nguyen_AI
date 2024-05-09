# Ex1: Write a NumPy program to reverse an array (first element becomes last).
# Input: [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]

import numpy as np
def reverse_array(input_array):
    """we use 2 solution: normal array and numpy array """
    # solution1: use normal array
    # i = 0
    # j = len(input_array) - 1
    # swap_array = input_array
    # while(True):
    #     if (i >= j):
    #         break
    #     else:
    #         swap_array[i], swap_array[j] = swap_array[j], swap_array[i]
    #         i += 1
    #         j -= 1

    # solution2: numpy array
    swap_array = np.array(input_array)
    swap_array = input_array[::-1]
    return swap_array

#---------------------------------------------------------------------------------------------------

# Ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array
# Input array1: [ 0 10 20 40 60]
#       array2: [10, 30, 40]


def check_element(array1, array2):
    """we have 2 solution: normal array and np array
    the first solution use normal array: we use interact 1 aray and check if this element is in other array ?
    the second solution use np array: we use intersection method
    """
    # result_array = []
    # for i in array1:
    #     if i in array2:
    #         result_array.append(i)
    array1 = np.array(array1)
    array2 = np.array(array2)
    result_array = np.intersect1d(array1, array2)
    return result_array

#---------------------------------------------------------------------------------------------------
# Ex3: Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array
# Input Array [1,6,4,8,9,-4,-2,11]

def get_indices_max_min(input_array):
    result = {}
    #solution1:
    # max_ele = max(input_array)
    # min_ele = min(input_array)
    # for i in range(len(input_array)):
    #     if input_array[i] == max_ele:
    #         max_ele_index = i
    #         result['max_ele'] = max_ele
    #         result['max_ele_index'] = max_ele_index
    #         result[max_ele] = max_ele_index
    #     if input_array[i] == min_ele:
    #         min_ele_index = i
    #         result['max_ele'] = max_ele
    #         result['max_ele_index'] = max_ele_index

    # solution2:
    input_array = np.array(input_array)
    max_ele_index = np.argmax(input_array)
    max_ele = input_array[max_ele_index]

    min_ele_index = np.argmin(input_array)
    min_ele = input_array[min_ele_index]

    result['min_ele'] = min_ele
    result['min_ele_index'] = min_ele_index
    result['max_ele'] = max_ele
    result['max_ele_index'] = max_ele_index
    return result

#---------------------------------------------------------------------------------------------------
# Ex4: Read the entire file story.txt and write a program to print out top 100 words occur most
# frequently and their corresponding appearance. You could ignore all
# punction characters such as comma, dot, semicolon, ...
# Sample output:
# house: 453
# dog: 440
# people: 312
# ...


import re
def find_top_100_words(file):
    pass
    with open(file = file, mode = 'r') as file:
        str_input = file.read()
        str_output = re.findall(r'\w+\'?\w?', str_input)
        words_set = set(str_output)
        count_words = {}
        for word in words_set:
            count_words[word] = str_output.count(word)
        count_words = sorted(count_words.items(), key = lambda key:key[1], reverse=True)

        return count_words

def main():
    while(True):
        print("----------------------------------------------------------")
        print("Enter you ex solution what you want to show:")
        print("Enter 1,2,3,4 to show the solution of ex1, ex2, ex3, ex4")
        print("Enter q to quit!")
        your_choice = input("Your choice:")
        print("----------------------------------------------------------")
        if your_choice == '1':
            input_array = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
                           35, 36, 37]
            result = reverse_array(input_array)
            print("Solv: Ex1: Write a NumPy program to reverse an array (first element becomes last).")
            print(result)
        elif your_choice == '2':
            print("ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array:")
            array1 = [0, 10, 20, 40, 60]
            array2 = [10, 30, 40]
            result = check_element(array1, array2)
            print(result)
        elif your_choice == '3':
            print("ex3: Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array")
            input_array = [1, 6, 4, 8, 9, -4, -2, 11]
            print(get_indices_max_min(input_array))

        elif your_choice == '4':
            count_words = find_top_100_words(file='story.txt')
            print(count_words)
            for i in range(100):
                print(f"the word \'{count_words[i][0]}\' occur {count_words[i][1]}")
        elif your_choice == 'q':
            break
        else:
            print("Please enter following the manual!")

main()
