# Ex1: Write a program to count positive and negative numbers in a list
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]

def count_positive_negative_number(data_list):
    """
    Given a list and count positive and negative numbers
    """
    positive_numbers = 0
    negative_numbers = 0
    for i in data_list:
        if i > 0:
            positive_numbers += 1
        if i < 0:
            negative_numbers += 1
        else:
            continue
    return (positive_numbers, negative_numbers)

# Ex2: Given a list, extract all elements whose frequency is greater than k.
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3

def freq_numbers_in_list(data_list):
    """
    In this function, We given a list, extract all elements, count frequency of each elements
    """
    # freq_numbers = {}
    freq_numbers_greater_k = {}
    for i in data_list:
        count = 0
        for j in data_list:
            if i == j:
                count += 1
            # freq_numbers[i] = count
                if count > 3:
                    freq_numbers_greater_k[i] = count
    return freq_numbers_greater_k

# Ex3: find the strongest neighbour. Given an array of N positive integers.
# The task is to find the maximum for every adjacent pair in the array.
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]

def strongest_neighbour(data_list):
    """
    Given a list, compare neighbour, return a list including: strongest neighbor
    """
    strongest_neighbour_list = []
    n = len(data_list)
    for i in range(0,n):
        try:
            if(data_list[i] < data_list[i+1]):
                strongest_neighbour_list.append(data_list[i+1])
            elif (data_list[i] >= data_list[i+1]):
                strongest_neighbour_list.append(data_list[i])
        except:
            print("something went wrong!")
    return strongest_neighbour_list

# Ex4: print all Possible Combinations from the three Digits
data4 = [1, 2, 3]

# n digit
def combination_three_number(data4):
    k = 1 # shitf 1 each time
    n = 3
    j = n - k # devide array input become to 2 array and combinator 2 array like mirror
    data = []
    x = data4
    for i in range(3):
        x = data4[j:] + data4[:j]
        # x = +x.join('')
        y = ''
        for a in x:
            y += str(a)
        data.append(y)
        # if you want to return a array, use  allow this line of code:
        # data.append(x)
        data4 = x

    return data


# Ex5: Given two matrices (2 nested lists), the task is to write a Python program
# to add elements to each row from initial matrix.
# For example: Input : test_list1 = [[4, 3, 5,], [1, 2, 3], [3, 7, 4]], test_list2 = [[1], [9], [8]]
# Output : [[4, 3, 5, 1], [1, 2, 3, 9], [3, 7, 4, 8]]
data5_list1 = [[4, 3, 5, ], [1, 2, 3], [3, 7, 4]]
data5_list2 = [[1, 3], [9, 3, 5, 7], [8]]

def matrix_additional(list1, list2):
    n = len(list1)
    for i in range(n+1):
        list3 = [0] * n
        print(list1[i])
        print(list2[i])
        list3[i] = list1[i] + list2(i)
    return list1

# Ex6:  Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Ex7: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Ex8: Let user type 2 words in English as input. Print out the output
# which is the shortest chain according to the following rules:
# - Each word in the chain has at least 3 letters
# - The 2 input words from user will be used as the first and the last words of the chain
# - 2 last letters of 1 word will be the same as 2 first letters of the next word in the chain
# - All the words are from the file wordsEn.txt
# - If there are multiple shortest chains, return any of them is sufficient

def main():
    #Ex1:
    # -------------------------------------------------------------------------
    print("Ex2: ")
    (positive_numbers, negative_numbers) = count_positive_negative_number(data1)
    print(positive_numbers, negative_numbers)
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Ex2: Given a list, extract all elements whose frequency is greater than k =3:
    print("Ex2: ")
    for key, value in freq_numbers_in_list(data2).items():
        print(f"The number {key} occurs {value} time in list")
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Ex3: find the strongest neighbour. Given an array of N positive integers.
    print("Ex3: Strongest neighbour is: ")
    print(strongest_neighbour(data3))
    # -------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #EX4:
    print("Ex4: print all Possible Combinations from the three Digits: ")
    result = combination_three_number(data4)
    print(result)

    #-----------------------------------------------------------------------
    #EX5:
    print("add elements to each row from initial matrix:")
    print(matrix_additional(data5_list1, data5_list2))
    #------------------------------------------------------------------------

main()
