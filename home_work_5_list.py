#ex1:
"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 list bao gồm các số bất kì
    2. 1 số tự nhiên k
    Trả về kết quả là 1 list, trong đó các phần tử bị dịch
    sang trái k đơn vị
    Ví dụ:
    Input:
        array = [1, 2, 3, 4, 5]
        k = 2
    Output:
        array = [3, 4, 5, 1, 2]
"""

# array = [1, 2, 3, 4, 5]
# k = 2

# cách 1:
# def shift_array(array, k):
#     if k > len(array):
#         k = len(array) - k
#     n = len(array) - k
#     new_array = array[k:] + array[:-k-1]
#     return(new_array)


# cách 2:
def shift_array(array, k):
    if k > len(array):
        k = len(array) - k
    new_array = [0] * len(array)
    for i in range(len(array)):
        new_array[i] = array[i-k]
    return(new_array)


# shift_array(array, k)

#ex2:
"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 list bao gồm các số bất kì
    2. 1 số tự nhiên k
    tách hàm ban đầu thành 2 nửa, được phân cách bởi
    phần tử có chỉ số là k (phần tử này sẽ thuộc về
    nửa thứ 2) rồi sau đó nối chúng lại sao cho nửa
    thứ 2 đứng ở trước nửa thứ nhất.
    Ví dụ:
    Input:
        array = [1, 2, 3, 4, 5]
        k = 3
    Output:
        array = [4, 5, 1, 2, 3]
"""

# array = [1, 2, 3, 4, 5]
# k = 3


def split_array(array, k):
    if k > len(array):
        k = len(array) - k
    new_array = array[k:] + array[:k]
    return new_array


# print(split_array(array, k))

# Ex3:
"""
    Viết 1 hàm nhận 2 tham số đầu vào là 2 ma trận,
    kết quả trả về là ma trận tổng của chúng. Nếu phép
    cộng không thực hiện được thì trả về giá trị 0
    Ví dụ:
    Input:
        mat1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    mat2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
    ]
    Output:
        # array = [4, 5, 1, 2, 3]

"""

mat1 = [
        [6,7,4],
        [6,8,6]
    ]

mat2 = [
        [1,5,4],
        [3,3,6]
        ]
def add_matrices(mat1, mat2):
    if (len(mat1) == len(mat2)) and len(mat1[0]) == len(mat2[0]):
        mat_tong = []
        temp_tong = 0
        n = len(mat1)
        k = len(mat1[0])

        for i in range(n):

            mat_tong.insert(i, [])
            for j in range(k):
                temp_tong = mat1[i][j] + mat2[i][j]
                mat_tong[i].insert(j, temp_tong)
        return mat_tong
    else:
        return 0

# print(add_matrices(mat1, mat2))

#EX4:
"""
    Viết 1 hàm nhận 2 tham số đầu vào là 2 ma trận cùng kích thước,
    kết quả trả về là ma trận tích của chúng
    Ví dụ:
    Input:
        mat1 = [
        [1, 2, 3],
        [4, 5, 6],
    ]
    mat2 = [
        [7, 8],
        [9, 10],
        [11, 12],
    ]
    Output:
        array = [
        [58,  64],
        [139, 154],
    ]

"""

mat1 = [
        [1, 2, 3], # i = 0 j = 0->2
        [4, 5, 6], # i = 1 j = 0->2
    ]
mat2 = [
        [7, 8],     # j = 0-> 2, i = 0 a[j][i]
        [9, 10],    # j = 0-> 2, i = 0 a[j][i]
        [11, 12],
    ]

def multiply_matrices(mat1, mat2):
    pass
    if len(mat1[0]) == len(mat2):
        pass
        ma_tran_tich = []
        n = len(mat1)
        k = len(mat1[0])
        q = len(mat2[0])
        for i in range(n):
            ma_tran_tich.insert(i, [])
            for j in range(q):
                tem_tich = 0
                for l in range(k):
                    tem_tich = tem_tich + mat1[i][l] * mat2[l][j]
                ma_tran_tich[i].insert(j, tem_tich)

        return ma_tran_tich
    else:
        return 0

# print(multiply_matrices(mat1, mat2))

# EX5:
"""
    Yêu cầu người dùng nhập vào 1 số nguyên dương
    Kiểm tra xem số đó có phải là 1 số may mắn hay không

    Số may mắn là số được định nghĩa theo quá trình sau: bắt đầu với số nguyên dương x
    và tính tổng bình phương y các chữ số của x, sau đó tiếp tục tính tổng bình phương
    các chữ số của y. Quá trình này lặp đi lặp lại cho đến khi thu được kết quả là 1
    thì dừng (tổng bình phương các chữ số của số 1 chính là 1) hoặc quá trình sẽ kéo dài vô tận.
    Số mà quá trình tính này kết thúc bằng 1 gọi là số may mắn.
    Số có quá trình tính kéo dài vô tận là số không may mắn hay còn gọi là số đen đủi
    Ví dụ: 19 là số may mắn vì
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1 (End)

    Some happy numbers are: 1, 6, 36, 44, 49, 79, 100, 160, 170, 216, 224, 229, 254,
    264, 275, 285, 289, 294, 335, 347, 355, 357, 388, 405
    1 vài số may mắn: 1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100

"""
# n = input("Enter a number: ")
import time
def lucky_number(n):
    start_time = time.time()
    temp_total_list = []
    while(True):
        k = len(str(n))
        total = 0
        n = str(n)
        for i in n:
            total = total + int(i)**2
            n = str(total)
        if total == 1:
            time_process = time.time() - start_time
            print("--- %s seconds ---" % time_process)
            return True
        elif total not in temp_total_list:
            temp_total_list.append(total)
        elif total in temp_total_list:
            time_process = time.time() - start_time
            print("--- %s seconds ---" % time_process)
            return False

# if(lucky_number(n)):
#     print(f"Your number {n} is a lucky number! ")
# else:
#     print(f"Your number {n} is not a lucky number! ")

# EX6:
"""
    Cho 1 danh sách gồm các số
    Viết các chương trình để tìm ra:
    1. Số lớn nhất
    2. Số lớn thứ nhì
    3. k số lớn nhất

"""

numbers = [20, 10, -4, 5, 15, 36, -16]

def find_max_second_third(numbers):
    # max_fist = max(numbers)
    # numbers.remove(max_fist)
    # max_seccond = max(numbers)
    # numbers.remove(max_seccond)
    # max_third = max(numbers)
    # max_fist_seccond_third = [max_fist, max_seccond, max_third]
    numbers = sorted(numbers)
    # print(numbers)
    return (numbers[-3:])

# print(find_max_second_third(numbers))

#EX7:
"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 list bao gồm các số bất kì
    2. 1 số tự nhiên k
    Đếm xem số k xuất hiện trong list bao nhiêu lần
"""

numbers = [20, 10, -4, 5, 10, 36, -16, 3, 5, 10, 16, -5, 5]
k = 10

def character_occurrences(numbers, k):
    character_occurrences = 0
    for i in numbers:
        if k == i:
            character_occurrences += 1
    return character_occurrences


# print(character_occurrences(numbers, k))

#EX8:
"""
    Viết 1 hàm nhận 2 tham số đầu vào:
    1. 1 list bao gồm các từ bất kì
    2. 1 số tự nhiên k
    In ra các từ trong list có độ dài lớn hơn k ký tự
"""

word_list = ["apple", "banana", "cherry", "date", "monkey", "blackpink"]
k = 5

def words_len_more_k(word_list, k):
    words = []
    for word in word_list:
        if len(word) > k:
            words.append(word)
    return words

# print(words_more_len(word_list,k))

#EX9:
"""
    Viết hàm nhận 1 tham số đầu vào là 1 số tự nhiên n
    In ra kết quả là tích các thừa số nguyên tố của số đó
    Ví dụ, với n = 100
    Kết quả in ra màn hình là:
        100 = 2 x 2 x 5 x 5
"""

# n = int(input("Enter your number: "))
def prompt_product_number_prime_numbers(n):
    list_prime_numbers = [i for i in range(2,n+1)]
    list_prime_of_number = []
    for i in range(1,n+1,1):
        for j in range(2,i,1):
            # print(f"i: {i} j: {j}")
            if i % j == 0:
                if i in list_prime_numbers:
                    list_prime_numbers.remove(i)

    while(True):
        for i in list_prime_numbers:
            if n % i == 0:
                list_prime_of_number.append(i)
                n /= i
            if n == 1:
                return list_prime_of_number

# print(prompt_product_number_prime_numbers(n))

