def max_width_length(array):
    """"
    input: array[clumns = 6] about flowers of specified species flowers
    output: set of max_SepalLength, max_SepalWidth
    """
    max_SepalLength = 0.0
    max_SepalWidth = 0.0
    for i in array:
        i[1] = float(i[1])
        i[2] = float(i[2])
        if max_SepalLength < (i[1]):
            max_SepalLength = i[1]
        if max_SepalWidth < (i[2]):
            max_SepalWidth = i[2]
    return(max_SepalLength, max_SepalWidth)

with open ("../../../../Bai_Tap_Buoi_2/Iris.csv") as file:
# Id,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm,Species
#  create 3 array contain flowers of each specified folowers
    setosa = []
    virginica = []
    versicolor = []
    for line in file:
        line = line.split(',')
        if line[5] == 'Iris-versicolor\n':
            versicolor.append(line)
        if line[5] == 'Iris-virginica\n':
            virginica.append(line)
        if line[5] == 'Iris-setosa\n':
            setosa.append(line)

    print(f"max_versicolor_SepalLength: {max_width_length(versicolor)[0]}")
    print(f"max_versicolor_SepalWidth: {max_width_length(versicolor)[1]}")
    print(f"max_virginica_SepalLength: {max_width_length(virginica)[0]}")
    print(f"max_virginica_SepalWidth: {max_width_length(virginica)[1]}")
    print(f"max_setosa_SepalLength: {max_width_length(setosa)[0]}")
    print(f"max_setosa_SepalWidth: {max_width_length(setosa)[1]}")




