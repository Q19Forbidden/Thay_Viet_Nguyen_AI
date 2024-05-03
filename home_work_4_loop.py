#ex1:
"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên
    1. Kiểm tra xem đó có phải là số nguyên tố hay không
    2. In ra màn hình tất cả các số nguyên tố nhỏ hơn hoặc bằng n
"""
# n = int(input("Enter a number: "))


def tim_so_nguyen_to(n):
    so_nguyen_to = []
    if n <= 1:
        return False
    elif n > 2:
        so_nguyen_to.append(2)

    for k in range(2, n + 1, 1):
        for i in range(2, k, 1):
            # print(k)
            if (k % i) == 0:
                break
            elif i == (k-1):
                so_nguyen_to.append(k)
    return so_nguyen_to


# print(tim_so_nguyen_to(n))

#ex2:
"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên n khác 0
    Tính n! theo 2 cách:
    - Sử dụng vòng lặp for
    - Sử dụng vòng lặp while
"""
# n = int(input("Enter a number: "))
def factorial_of_n(n):
    result = 1
    for i in range(1, n+1, 1):
        result *= i
    print("Giai thừa của", n, "là", result)


# ex3:
"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên n khác 0
    In ra n số Fibonacci đầu tiên
    Định nghĩa dãy Fibonacci: Dãy Fibonacci bắt đầu với 2 số 1
    Các số sau được xác định bẳng tồng của 2 số ngay trước nó.
    1 vài số Fibonacci đầu tiên trong dãy: 1, 1, 2, 3, 5, 8
"""
# num = int(input("Enter a number: "))
def fibonacci(n):
    fibonaccis = [1, 1]
    if n > 0:
        for i in range(n):
            k = len(fibonaccis)
            # print(k)
            fibo = fibonaccis[k-2] + fibonaccis[k-1]
            fibonaccis.append(fibo)
            if(len(fibonaccis)  == n):
                return fibonaccis

# print(fibonacci(num))
# print(len(fibonacci(num)))

#ex4:
"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên n khác 0
    In ra tất cả các số Armstrong nhỏ hơn hoặc bằng n
    Định nghĩa số Armstrong: 1 số n được gọi là số Armstrong nếu:
    Tổng các chữ số của số đó, với mỗi chữ số được lũy thừa với
    số mũ k bằng chính số đó, với k là số chữ số của n
    Ví dụ: 153 là số Amstrong vì:
    153 có 3 chữ số, và 153 = 1^3 + 5^3 + 3^3
"""
# n = input("Enter a number: ")

def amstrong(n):
    k = len(n)
    sum = 0
    for i in range(k):
        sum += int(n[i])**k
    print(sum)
    if sum == int(n):
        return True
    else:
        return False

# print(amstrong(n))

#ex4:
"""
    Đếm số chẵn, lẻ, âm, dương trong dãy sau
"""
# numbers = [2, -3, 1, 5, -6, 3, 2, -4, 0, 5, 1, -3, -1, 2, 6, 3, -5, 0, 1, -4, 2, 3, -1, 0, 3, 2, -4, 2, 3]

def even_odd_negative_positive(numbers):
    evens = []
    odds = []
    negatives = []
    positives = []
    for i in numbers:
        if i == 0:
            pass
        elif i > 0:
            positives.append(i)
        elif i < 0:
            negatives.append(i)

        if i == 0:
            pass
        elif i % 2 == 0:
            evens.append(i)
        elif i % 2 != 0:
            odds.append(i)
    # even = len(evens)
    # odd = len(odds)
    # negative = len(negatives)
    # positive = len(positives)
    return(evens, odds, negatives, positives)


# print(numbers)
# print(f"even: {even_odd_negative_positive(numbers)[0]} \r\nodd: {even_odd_negative_positive(numbers)[1]} \r\nnegative: {even_odd_negative_positive(numbers)[2]} \r\npositive: {even_odd_negative_positive(numbers)[0]}")

#ex6:
"""
    Yêu cầu người dùng nhập vào 1 số dạng nhị phân (e.g. 1001)
    In ra giá trị dạng thập phân tương ứng của số đó
"""
# n = input("Enter a binary number: ")
def conver_binary_to_decimal(n):
    k = len(n)
    total = 0
    j = 0
    for i in range(k-1, -1, -1):
        total += int(n[i]) * (2**j)
        j += 1
    return total

# print(f"binary: {n} convert to decimal is: {conver_binary_to_decimal(n)}")

#ex7:
"""
    Tìm số lớn nhất và nhỏ nhất trong dãy sau
"""
# numbers = [-9, 2, 10, -3, 1, 5, -6, 3, 2, -4, 0, 5, 1, -3, -1, 2, 6, 3, -5, 0, 1, -4, 2, 3, -1, 0, 3, 2, -4, 2, 3]


def max_min_in_list(numbers):
    max_of_list = numbers[0]
    min_of_list = numbers[1]
    for i in numbers:
        if i > max_of_list:
            max_of_list = i
        if i < min_of_list:
            min_of_list = i

    return min_of_list, max_of_list


# print(f"In this numbers: {numbers} \r\nmin is: {max_min_in_list(numbers)[0]}, \r\nmax is: {max_min_in_list(numbers)[1]}")

#ex8:
"""
    Cho 1 mảng gồm các số tùy ý
    Kiểm tra xem mảng đó có phải mảng đơn điệu hay không.
    Định nghĩa mảng đơn điệu: mảng đơn điệu là mảng
    không tăng hoặc không giảm
"""
array = [1, 3, 3, 4, 6, 7, 7]
# array = [5, 3, 2, 2, 1]
# array = [2, 3, 2, 1]

def monotonic_array(array):
    k = len(array)
    increasing_counter = 0
    ascending_counter = 0
    for i in range(k):
        if array[i] >= array[i - 1]:
            increasing_counter += 1

        if array[i] <= array[i - 1]:
            ascending_counter += 1

    print(f"increasing_counter: {increasing_counter}")
    print(f"ascending_counter: {ascending_counter}")

    if increasing_counter == (k - 1):
        print(f"mảng {array} là mảng đơn điệu tăng dần")
    elif ascending_counter == (k - 1):
        print(f"mảng {array} là mảng đơn điệu giảm dần")
    else:
        print(f"mảng {array} không là mảng đơn điệu")

# monotonic_array(array)

# ex7:
"""
    In ra các số có ít hơn 4 chữ số và chia hết cho cả 5 và 7
"""

def three_digit_numbers_divisible_by_5_and_7():
    three_digit_numbers_divisible_by_both_5_and_7 = []
    for i in range(1000):
        if i % 35 == 0:
            three_digit_numbers_divisible_by_both_5_and_7.append(i)
    print(f"Three digit numbers divisible by both 5 and 7 are: {three_digit_numbers_divisible_by_both_5_and_7}")


three_digit_numbers_divisible_by_5_and_7()