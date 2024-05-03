# Ex1:
"""
    Nhập vào 2 số:
    - 1 số đại diện cho 1 năm
    - 1 số đại diện cho 1 tháng trong năm đó
    In ra màn hình số ngày của tháng đó
    Chú ý: Năm nhuận là năm thỏa mãn 1 trong 2 điều kiện sau:
    - Năm đó chia hết cho 4 nhưng không chia hết cho 100
    - Năm đó chia hết cho 400
    Chi tiết số ngày trong tháng được tính như sau
    - Trong một năm, có 7 tháng sở hữu 31 ngày: tháng 1, tháng 3, tháng 5, tháng 7, tháng 8, tháng 10 và tháng 12.
    - Các tháng còn lại, tháng 4, tháng 6, tháng 9 và tháng 11, đều tự hào với 30 ngày.
    - Tháng 2, tháng thiếu, thường chỉ có 28 ngày vào năm không nhuận, hoặc có 29 ngày vào năm nhuận.
"""

def is_int(n):
        try:
            n = float(n)
            if (n - int(n) == 0):
                return True
        except ValueError:
            return False

def prompt_total_days_in_month():
    try:
        while (True):
            year = input("Enter year number: ")
            if is_int(year):
                year = int(year)
                if(year > 0):
                    break
        while(True):
            month = input("Enter month number: ")
            if (is_int(month)):
                month = int(month)
                if month in range(0,13,1):
                    break

        if month in [1,3,5,7,8,10,12]:
            print(f"Tổng số ngày trong tháng {month} là 31 ngày")
        elif month in [4,6,9,11]:
            print(f"Tổng số ngày trong tháng {month} là 30 ngày")
        elif month == 2:
            # check tháng 2
            if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
                print(f"Năm {year} là năm nhuận, nên tổng số ngày trong tháng {month} là 28 ngày")
            else:
                print(f"Tổng số ngày trong tháng {month} là 29 ngày")
    except ValueError:
        print("somthing went wrong!")
        return False
# Ex2:
"""
    Yêu cầu người dùng nhập vào 3 số a, b, c
    Tìm nghiệm của phương trình bậc 2
    ax^2 + bx + c = 0
"""
# a = float(input("Enter a: "))
# b = float(input("Enter b: "))
# c = float(input("Enter c: "))

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
def solutions_of_quadratic_equation():
    print("Enter a: ")
    a = get_number()
    print("Enter b: ")
    b = get_number()
    print("Enter c: ")
    c = get_number()

    if(a == 0):
        if( b == 0 and c == 0):
            print("Phương trình có vô số nghiệm")
        elif (b == 0 and c != 0):
            print("Phương trình vô nghiệm")
    if (a > 0):
        delta = b**2 - 4*a*c
        if delta < 0:
            print("Phương trình vô nghiệm")
        elif delta == 0:
            x = -b/(2*a)
            print("phương trình có 2 nghiệm kép")
            print(f"x = {x}")
        elif delta > 0:
            print("Phương trình có 2 nghiệm phân biệt")
            x1 = (-b + delta**0.5)/(2*a)
            x2 = (b + delta**0.5)/(2*a)
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")

# Ex3:
"""
    Yêu cầu người dùng nhập vào 1 số tự nhiên tương ứng
    với số đơn vị điện sử dụng của 1 hộ gia đình
    Viết chương trình tính hóa đơn tiền điện cho gia đình đó,
    với quy tắc sau:
    Số đơn vị điện                     Giá
    100 đơn vị đầu                  Miễn phí
    100 đơn vị tiếp theo            5$/đơn vị
    Các đơn vị sau đó               10$/đơn vị
"""
def calculate_electricity_bill():
    print("Nhập vào số điện của gia đình bạn trong tháng:", end="")
    electricity_consumption = get_number()
    if(electricity_consumption <= 100):
        electricity_bill = 0
        print(f"Số đơn vị điện của gia đình bạn là: {electricity_consumption} nên gia đình bạn được miễn phí điện")
    elif(200 >= electricity_consumption > 100):
        electricity_bill = 5 * (electricity_consumption - 100)
        print(f"Số đơn vị điện của gia đình bạn là {electricity_consumption}, số tiền phải nộp là {electricity_bill}$")
    elif(electricity_consumption > 200):
            electricity_bill = 10 * (electricity_consumption - 200) + 5 * (electricity_consumption - 100)
            print(f"Số đơn vị điện của gia đình bạn là {electricity_consumption}, số tiền phải nộp là {electricity_bill}$")
# Ex4:
"""
    Nhập vào điểm của 1 học sinh (0-100)
    Quy đổi điểm từ thang điểm 100 sang thang điểm chữ theo quy tắc:
        Điểm                             Quy đổi
        > 90                                A
        > 80 và <=90                        B
        > 60 và <= 80                       C
        <= 60                               D
"""
def convert_grades():
    print("Nhập vào điểm của học sinh: ", end="")
    score = get_number()
    if score > 90:
        print(f"Số điểm của bạn là {score} điểm, bạn đạt mức A")
    elif 90 >= score > 80:
        print(f"Số điểm của bạn là {score} điểm, bạn đạt mức B")
    elif 80 >= score > 60:
        print(f"Số điểm của bạn là {score} điểm, bạn đạt mức C")
    elif score < 60:
        print(f"Số điểm của bạn là {score} điểm, bạn đạt mức D")

# Ex5:
"""
    Yêu cầu người dùng nhập vào 3 số nguyên dương
    1. Kiểm tra xem đây có phải là số đo 3 cạnh của 1 tam giác không?
    2. Nếu có thì kiểm tra tiếp xem đây là tam giác cân, tam giác đều,
    tam giác vuông hay tam giác thường
    3. Kiểm tra tiếp xem tam giác có góc tù hay không?
    4. Tính diện tích của tam giác
"""
from math import sqrt
def calculate_triangle_area(a,b,c):
    q = (a + b + c)/2
    s = sqrt(q * (q - a) * (q - b) * (q - c))
    return s

def check_type_triangle():
    print("Nhập vào lần lượt số đo 3 cạnh của tam giác: ")
    print("Nhập vào số đo cạnh thứ nhất: ", end="")
    a = get_number()
    print("Nhập vào số đo cạnh thứ nhất: ", end="")
    b = get_number()
    print("Nhập vào số đo cạnh thứ nhất: ", end="")
    c = get_number()
    if ((a + b)> c or (b + c) > a or (a + c) > b):
        # print("Đây là số đo 3 cạnh của 1 tam giác")
        if (a == b == c):
            print(f"Với số đo 3 cạnh lần lượt là {a} {b} {c} Đây là số đo 3 cạnh của 1 tam giác đều")
        elif ((a == b ) or (b == c) or  (a == c)):
            if (((a ** 2 + b ** 2) == c**2) or ((a ** 2 + c ** 2) == b ** 2) or ((b ** 2 + c ** 2) == a ** 2) ):
                print(f"Với số đo 3 cạnh lần lượt là {a} {b} {c} Đây là số đo 3 cạnh của 1 tam giác vuông cân")
        elif (((a ** 2 + b ** 2) == c**2) or ((a ** 2 + c ** 2) == b ** 2) or ((b ** 2 + c ** 2) == a ** 2) ):
            print(f"Với số đo 3 cạnh lần lượt là {a} {b} {c} Đây là số đo 3 cạnh của 1 tam giác vuông")
        else:
            print(f"Với số đo 3 cạnh lần lượt là {a} {b} {c} Đây là số đo 3 cạnh của 1 tam giác thường")

        if (((a ** 2 + b ** 2) < c**2) or ((a ** 2 + c ** 2) < b ** 2) or ((b ** 2 + c ** 2) < a ** 2)):
            print(f"Với số đo 3 cạnh lần lượt là {a} {b} {c} tam giác này có góc tù")
        else:
            print("Tam giác không có góc tù")
        area = calculate_triangle_area(a, b, c)
        print(f"Diện tích của tam giác là {area}")

#EX6:
"""
    Yêu cầu người dùng nhập vào lượng nước tiêu thụ của 1 hộ gia đình
    Viết chương trình tính hóa đơn tiền nước cho gia đình đó,
    với quy tắc sau:
    Lượng nước (lít)                    Giá mỗi 1000 lít
    0-8000                                  5$
    8001-22000                              6$
    22001-30000                             7$
    30001+                                  10$
"""

def calculate_water_bill():
    print("Nhập vào số nước của gia đình bạn trong tháng:", end="")
    water_number = get_number()
    water_bill = 0
    if (0 <= water_number <= 8000):
        water_bill = 5 * water_number
    elif (8000 < water_number <= 22000):
        water_bill = 6 * water_number
    elif (22001 < water_number <= 30000):
        water_bill = 7 * water_number
    elif (30000 < water_number):
        water_bill = 10 * water_number
    else:
        print("Something went wrong!")
    print(f"Với số nước {water_number}, Hoá đơn tiền nước của nhà bạn là {water_bill}")

#EX7:
"""
    Yêu cầu người dùng nhập vào 2 số, trong đó:
    - Số thứ nhất là bán kính của 1 hình tròn
    - Số thứ hai là diện tích của 1 hình vuông
    Hãy tính và so sánh xem, trong 2 hình trên,
    hình nào có chu vi lớn hơn
"""
from math import pi
def compare_perimeters_both_circle_square():
    print("Nhập vào bán kính của hình tròn:", end="")
    r = get_number()
    print("Nhập vào diện tích hình vuông:", end="")
    s_square = get_number()

    q_circle = 2 * pi * r
    q_squre = sqrt(s_square) * 4
    if (q_circle > q_squre):
        print(f"Hình tròn có bán kính {r} và hình vuông có diện tích {s_square}, hình tròn có chu vi lớn hơn")
    elif(q_circle < q_squre):
        print(f"Hình tròn có bán kính {r} và hình vuông có diện tích {s_square}, hình vuông có chu vi lớn hơn")
    else:
        print(f"Hình tròn có bán kính {r} và hình vuông có diện tích {s_square}, 2 hình có chu vi bằng nhau")

def main():
    #EX1:
    print("This is function find the total number of days in specific month in year")
    prompt_total_days_in_month()

    #EX2:
    print("This is function find the solutions of the quadratic equation")
    solutions_of_quadratic_equation()

    #EX3:
    print("This is function Calculate electricity bill:")
    calculate_electricity_bill()

    #EX4:
    print("This is a function to convert students' scores from a 100-point scale to letter grades A, B, C, D")
    convert_grades()

    #EX5:
    print("A function to check what type of triangle it is and calculate area: ")
    check_type_triangle()

    #EX6:
    print("This is function Calculate water bill:")
    calculate_water_bill()

    #EX6:
    print("This is function compare perimeters of both circle and square:")
    compare_perimeters_both_circle_square()

if __name__ == "__main__":
    main()
