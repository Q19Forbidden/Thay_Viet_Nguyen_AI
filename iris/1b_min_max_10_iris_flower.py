def top_10_iris(array):
    """"
    input: an array about feature of iris flower include 6 elements
    output: 2 arrays about top 10 length and top 10 width in mm
    """
    SepalWidthCm = []
    SepalLengthCm = []
    for i in array:
        SepalLengthCm.append(i[1])
        SepalWidthCm.append(i[2])

    SepalLengthCm = sorted(SepalLengthCm,reverse=True)
    SepalWidthCm = sorted(SepalWidthCm,reverse=True)
    return(SepalLengthCm[:10], SepalWidthCm[:10])

with open ("../../../../Bai_Tap_Buoi_2/Iris.csv") as file:
# Iris.csv file include 150 iris flowers, has 6 feature: Id,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species
    setosa = []
    virginica = []
    versicolor = []
    for line in file:
        array = line.split(",")
        if array[5] == 'Iris-setosa\n':
            setosa.append(array)
        if array[5] == 'Iris-virginica\n':
            virginica.append(array)
        if array[5] == 'Iris-versicolor\n':
            versicolor.append(array)

    # print top 10 setosa
    print(f"top_10_Leng_irissetosa: {top_10_iris(setosa)[0]}")
    print(f"top_10_width_irissetosa: {top_10_iris(setosa)[1]}")

    # print top 10 virginica
    print(f"top_10_Leng_virginica: {top_10_iris(virginica)[0]}")
    print(f"top_10_width_virginica: {top_10_iris(virginica)[1]}")

    # print top 10 versicolor
    print(f"top_10_Leng_versicolor: {top_10_iris(versicolor)[0]}")
    print(f"top_10_width_versicolor: {top_10_iris(versicolor)[1]}")




