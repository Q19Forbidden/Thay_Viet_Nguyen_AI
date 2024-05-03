#ex1:
"""
    Yêu cầu người dùng nhập vào 1 số nguyên dương.
    Viết 1 hàm nhận tham số đầu vào là 1 số nguyên dương.
    Hàm này trả về hiệu số giữa số lớn nhất và số nhỏ nhất có thể tạo thành
    từ các chữ số của tham số đầu vào
    Ví dụ, nếu tham số đầu vào là 314, thì giá trị trả về của hàm số
    là 297, vì 297 = 431 - 134
"""

def check_positive_integers(n):
    if (n.isdigit() and int(n) > 0):
            return True
    else:
        return False

def max_diff(n):
    if (check_positive_integers(n)):
        min_n = "".join(sorted(n))
        max_n = "".join(sorted(n)[::-1])
        return int(max_n) - int(min_n)


# number = input("Enter a number: ")
# print(f"The difference between the largest and smallest numbers is {max_diff(number)}")


#ex2:
"""
    Pascal's triangle
    Yêu cầu người dùng nhập vào 1 số nguyên dương n.
    Viết 1 hàm nhận tham số đầu vào là số nguyên dương n.
    Hàm này tạo ra tam giác pascal cho tới hàng thứ n
    Ví dụ nếu n = 4 thì hàm sẽ in ra kết quả sau:
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
"""


def pascals_triangle(rows):
    if check_positive_integers(rows):
        rows = int(rows)
        pascals = [[1, 1]]
        if rows == 1:
            pascals = pascals
        elif rows > 1:
            for i in range(1, rows):
                pascals.insert(i,[])
                for j in range(0, i + 2):
                    if (j == 0):
                        pascals[i].insert(j, 1)
                    elif (j != 0):
                        if (j == (i + 1)):
                            pascals[i].insert(j, 1)
                        else:
                            pascals[i].insert(j,pascals[i-1][j-1]+ pascals[i-1][j])
        return (pascals)


# n = input("Enter a number: ")
# pascals = pascals_triangle(n)
# for row in pascals:
#     print(row)

#ex3:
"""
    Cho 1 dãy số đầu vào là các số liên tiếp từ 1 đến n, trong đó có
    1 số bị khuyết.
    Viết 1 hàm nhận dãy số này là tham số đầu vào, và trả lại giá trị bị khuyết
"""


def find_missing_value(array):
    n = array[-1]
    array1 = [i for i in range(1,n+1)]
    set_array = set(array)
    set_array1 = set(array1)
    missing_value = set_array1.difference(set_array)
    return missing_value

# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16]
# missing_value = find_missing_value(array)
# print(missing_value)

#ex4:
"""
    Viết 1 hàm kiểm tra xem 1 mảng 2 chiều (nested list) có phải là
    magic square (ma phương) hay không?
    Hàm nhận tham số đầu vào là 1 nested list, và trả về
    True nếu đó là ma phương, hoặc False nếu không phải

    Định nghĩa:
    một ma trận kì ảo bậc n (còn gọi là ma phương)
    là một cách sắp xếp n² số, là các số nguyên phân biệt,
    trong một bảng vuông sao cho tổng n số trên mỗi hàng, cột,
    và đường chéo đều bằng nhau.
"""


def is_magic_square(matrix):
    n = len(matrix)
    list_sum = []
    sum_main_diagonal = 0
    sum_spare_diagonal = 0
    for i in range(n):
        sum_row = 0
        sum_col = 0
        sum_main_diagonal += matrix[i][i]       # kiểm tra tổng đường chéo chính
        sum_spare_diagonal += matrix[n-i-1][i]  # kiểm tra tổng đường chéo phụ
        for j in range(n):
            if matrix[i][j] > n**2:
                return False
            sum_row += matrix[i][j]             # kiểm tra tổng các hàng
            sum_col += matrix[j][i]              # kiểm tra tổng các cột

        list_sum.append(sum_row)
        list_sum.append(sum_col)
    list_sum.append(sum_main_diagonal)
    list_sum.append(sum_spare_diagonal)

    if (max(list_sum) != min(list_sum)):
        return False
    else:
        return True

matrix1 = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]
print(is_magic_square(matrix1))     # True
matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(is_magic_square(matrix2))     # False
matrix3 = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]
print(is_magic_square(matrix3))     # True