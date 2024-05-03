# Ex1:
"""
    Yêu cầu người dùng nhập vào bán kính của hình tròn.
    Tính và hiển thị ra màn hình chu vi và diện tích của
    hình tròn tương ứng
"""
from math import pi
def is_number(n):
    try:
        n = float(n)
        return True
    except ValueError:
        return False
def get_number():
    while True:
        r = input()
        if r.strip() and is_number(r):
            return float(r)
        print("Invalid number")

def calculate_perimeter_area(r):
    # Perimeter of circle
    c = 2 * pi * r
    # Area of circle
    s = pi * r**2
    return c, s

# -------------------------------------------------------------------------
#EX3:
"""
    Yêu cầu người dùng nhập vào 1 số nguyên tương ứng với số giờ
    In ra số giây tương ứng
"""
def calculate_second_from_hours(h):
    second = h * 3600
    return second

# -------------------------------------------------------------------------
#EX4:
"""
    Yêu cầu người dùng nhập vào 1 số nguyên n
    Tính và in ra tổng số đo các góc của đa giác đều n cạnh
"""
def calculate_degrees_angles(n):
    return (n-2)*180

# -------------------------------------------------------------------------
#EX5:
"""
    Nhập vào số giây bất kỳ t (t là số nguyên dương nhỏ hơn hoặc bằng 86400)
    In ra màn hình thời gian tương ứng dưới dạng hh:mm:ss
"""
def calculate_time(n):
    h = int(n / 3600)
    m = int((n - h*3600)/60)
    s = n % 60
    return h, m, s

# -------------------------------------------------------------------------
#EX6:
"""
    Đội Manchester United tham gia giải ngoài hạng anh.
    Yêu cầu người dùng nhập vào lần lượt 3 số tự nhiên
    tương ứng với số trận thắng, hòa, thua của đội.
    Quy tắc tính điểm như sau:
    - Mỗi trận thắng đội sẽ được 3 điểm
    - Mỗi trận hòa đội sẽ được 1 điểm
    - Mỗi trận thua đội sẽ không được điểm nào
    Tính số điểm đội có được
"""
def points(w, d, l):
    point = w * 3 + d * 1 + l * 0
    return point

# -------------------------------------------------------------------------
#EX7:
"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên bất kì
    Lấy ra chữ số hàng đơn vị theo 2 cách khác nhau
    rồi in ra màn hình
"""
def get_digit(n):
    # Method 1
    n = int(n)
    digit = n % 10
    # Method 2
    # n = str(n)
    # digit = n[-1]
    return digit
# -------------------------------------------------------------------------
#EX8:
"""
    Yêu cầu người dùng nhập vào 2 số bất kỳ.
    Viết chương trình để đổi giá trị 2 số đó với nhau theo 2 cách
"""
def swap_value(a,b):
    # Method 1
    tmp = a
    a = b
    b = tmp
    # Method 2
    return a, b


# a = input("Enter the first value: ")
# b = input("Enter the second value: ")
# print("Original values: a =", a, ", b=", b)

def main():
    # Ex1:
    # -------------------------------------------------------------------------
    # print("calculate the perimeter and area with radius: ")
    # print("Please Enter you radius: ")
    # r = get_number()
    # c, s = calculate_perimeter_area(r)
    # print(f"The circle with radius is {r}")
    # print(f"perimeter: {c}")
    # print(f"area: {s}")
    # -------------------------------------------------------------------------

    # Ex3:
    # -------------------------------------------------------------------------
    # print("calculate how many seconds with a number hours: ")
    # print("Please Enter you hours: ")
    # h = get_number()
    # seconds = calculate_second_from_hours(h)
    # print(f"{h} hours mean {seconds} seconds")
    # -------------------------------------------------------------------------

    # Ex4:
    # -------------------------------------------------------------------------
    # print("calculate sum of all angles of triangle: ")
    # print("Please Enter you hours: ")
    # n = get_number()
    # sum_degrees = calculate_degrees_angles(n)
    # print(f"Đa giác {n} cạnh có tổng số đo các góc là {sum_degrees} độ ")

    # Ex5:
    # -------------------------------------------------------------------------
    # print("calculate time in hh: mm : ss: ")
    # print("Please Enter you time: ")
    # n = get_number()
    # h, m, s = calculate_time(n)
    # print(f"{h} hours: {m} minutes {s} seconds ")
    # -------------------------------------------------------------------------

    # EX6:
    # print("calculate points of your team: ")
    # print("Please Enter win number: ")
    # w = get_number()
    # print("Please Enter draw number: ")
    # d = get_number()
    # print("Please Enter lose number: ")
    # l = get_number()
    #
    # point = points(w, d, l)
    # print(f" Your team has {point} with {w} wins, {d} draws, {l} loses")

    # -------------------------------------------------------------------------
    # EX7:
    # print("Please Enter your number which you want to get digit: ")
    # n = get_number()
    # digit = get_digit(n)
    # print(digit)

    # EX8:
    print("Please Enter your first number which you want to swap: ")
    a = int(get_number())
    print("Please Enter your first number which you want to swap: ")
    b = int(get_number())
    print(f"Original numbers: a= {a}, b = {b}")
    a, b = swap_value(a, b)
    print(f"After swap: a = {a}, b = {b}")

if __name__ == "__main__":
    main()
